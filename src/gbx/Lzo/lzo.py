import math

class LZO1x:
    blockSize = 4096

    OK = 0
    INPUT_OVERRUN = -4
    OUTPUT_OVERRUN = -5
    LOOKBEHIND_OVERRUN = -6
    EOF_FOUND = -999

    def __init__(self):
        # Working buffers and state
        self.buf = None        # input buffer (bytearray)
        self.out = None        # output buffer (bytearray)
        self.cbl = 0           # current length of out buffer
        self.ip_end = 0
        self.op_end = 0
        self.t = 0

        self.ip = 0
        self.op = 0
        self.m_pos = 0

        self.skipToFirstLiteralFun = False

        self.state = None
        self.dict = None

    def ctzl(self, v):
        # Count trailing zero bits for a 32-bit integer.
        if v & 1:
            return 0
        else:
            c = 1
            if (v & 0xffff) == 0:
                v >>= 16
                c += 16
            if (v & 0xff) == 0:
                v >>= 8
                c += 8
            if (v & 0xf) == 0:
                v >>= 4
                c += 4
            if (v & 0x3) == 0:
                v >>= 2
                c += 2
            c -= v & 0x1
            return c

    def extendBuffer(self):
        new_len = self.cbl + self.blockSize
        newBuffer = bytearray(new_len)
        newBuffer[:len(self.out)] = self.out
        self.out = newBuffer
        self.cbl = new_len
        # Also update state output buffer if needed.
        self.state['outputBuffer'] = self.out

    def eof_found(self):
        return 0 if self.ip == self.ip_end else (-8 if self.ip < self.ip_end else -4)

    def match_next(self):
        while self.op + 3 > self.cbl:
            self.extendBuffer()
        self.out[self.op] = self.buf[self.ip]
        self.op += 1
        self.ip += 1
        if self.t > 1:
            self.out[self.op] = self.buf[self.ip]
            self.op += 1
            self.ip += 1
            if self.t > 2:
                self.out[self.op] = self.buf[self.ip]
                self.op += 1
                self.ip += 1
        self.t = self.buf[self.ip]
        self.ip += 1

    def match_done(self):
        self.t = self.buf[self.ip - 2] & 3
        return self.t

    def copy_match(self):
        self.t += 2
        while self.op + self.t > self.cbl:
            self.extendBuffer()
        # Copy in 4-byte chunks when possible (simulate 32-bit copy)
        if self.t > 4 and (self.op % 4 == self.m_pos % 4):
            # copy until self.op is aligned
            while (self.op % 4) and self.t > 0:
                self.out[self.op] = self.out[self.m_pos]
                self.op += 1
                self.m_pos += 1
                self.t -= 1
            # now copy 4 bytes at a time
            while self.t >= 4:
                self.out[self.op:self.op+4] = self.out[self.m_pos:self.m_pos+4]
                self.op += 4
                self.m_pos += 4
                self.t -= 4
        # copy any remaining bytes
        while self.t > 0:
            self.out[self.op] = self.out[self.m_pos]
            self.op += 1
            self.m_pos += 1
            self.t -= 1

    def copy_from_buf(self):
        while self.op + self.t > self.cbl:
            self.extendBuffer()
        if self.t > 4 and (self.op % 4 == self.ip % 4):
            while (self.op % 4) and self.t > 0:
                self.out[self.op] = self.buf[self.ip]
                self.op += 1
                self.ip += 1
                self.t -= 1
            while self.t >= 4:
                self.out[self.op:self.op+4] = self.buf[self.ip:self.ip+4]
                self.op += 4
                self.ip += 4
                self.t -= 4
        while self.t > 0:
            self.out[self.op] = self.buf[self.ip]
            self.op += 1
            self.ip += 1
            self.t -= 1

    def match(self):
        while True:
            if self.t >= 64:
                self.m_pos = self.op - 1
                self.m_pos -= (self.t >> 2) & 7
                self.m_pos -= self.buf[self.ip] << 3
                self.ip += 1
                self.t = (self.t >> 5) - 1

                self.copy_match()

                if self.match_done() == 0:
                    break
                else:
                    self.match_next()
                    continue

            elif self.t >= 32:
                self.t &= 31
                if self.t == 0:
                    while self.buf[self.ip] == 0:
                        self.t += 255
                        self.ip += 1
                    self.t += 31 + self.buf[self.ip]
                    self.ip += 1
                self.m_pos = self.op - 1
                self.m_pos -= (self.buf[self.ip] >> 2) + (self.buf[self.ip + 1] << 6)
                self.ip += 2

            elif self.t >= 16:
                self.m_pos = self.op
                self.m_pos -= (self.t & 8) << 11
                self.t &= 7
                if self.t == 0:
                    while self.buf[self.ip] == 0:
                        self.t += 255
                        self.ip += 1
                    self.t += 7 + self.buf[self.ip]
                    self.ip += 1
                self.m_pos -= (self.buf[self.ip] >> 2) + (self.buf[self.ip + 1] << 6)
                self.ip += 2
                if self.m_pos == self.op:
                    self.state['outputBuffer'] = self.out[:self.op]
                    return self.EOF_FOUND
                self.m_pos -= 0x4000

            else:
                self.m_pos = self.op - 1
                self.m_pos -= self.t >> 2
                self.m_pos -= self.buf[self.ip] << 2
                self.ip += 1

                while self.op + 2 > self.cbl:
                    self.extendBuffer()
                self.out[self.op] = self.out[self.m_pos]
                self.op += 1
                self.out[self.op] = self.out[self.m_pos + 1]
                self.op += 1

                if self.match_done() == 0:
                    break
                else:
                    self.match_next()
                    continue

            self.copy_match()

            if self.match_done() == 0:
                break

            self.match_next()

        return self.OK

    def decompress(self, state):
        self.state = state
        # Make sure buf is mutable and pad to a multiple of 4.
        self.buf = bytearray(state['inputBuffer'])
        pad = (4 - (len(self.buf) % 4)) % 4
        self.buf += bytearray(pad)

        # Prepare an output buffer padded to a multiple of blockSize.
        pad2 = (self.blockSize - (len(self.buf) % self.blockSize)) % self.blockSize
        self.out = bytearray(len(self.buf) + pad2)
        self.cbl = len(self.out)
        state['outputBuffer'] = self.out

        self.ip_end = len(self.buf)
        self.op_end = len(self.out)
        self.t = 0

        self.ip = 0
        self.op = 0
        self.m_pos = 0

        self.skipToFirstLiteralFun = False

        # First literal run?
        if self.buf[self.ip] > 17:
            self.t = self.buf[self.ip] - 17
            self.ip += 1
            if self.t < 4:
                self.match_next()
                ret = self.match()
                if ret != self.OK:
                    return self.OK if ret == self.EOF_FOUND else ret
            else:
                self.copy_from_buf()
                self.skipToFirstLiteralFun = True

        while True:
            if not self.skipToFirstLiteralFun:
                self.t = self.buf[self.ip]
                self.ip += 1
                if self.t >= 16:
                    ret = self.match()
                    if ret != self.OK:
                        return self.OK if ret == self.EOF_FOUND else ret
                    continue
                if self.t == 0:
                    while self.buf[self.ip] == 0:
                        self.t += 255
                        self.ip += 1
                    self.t += 15 + self.buf[self.ip]
                    self.ip += 1
                self.t += 3
                self.copy_from_buf()
            else:
                self.skipToFirstLiteralFun = False

            self.t = self.buf[self.ip]
            self.ip += 1
            if self.t < 16:
                self.m_pos = self.op - (1 + 0x0800)
                self.m_pos -= self.t >> 2
                self.m_pos -= self.buf[self.ip] << 2
                self.ip += 1
                while self.op + 3 > self.cbl:
                    self.extendBuffer()
                self.out[self.op] = self.out[self.m_pos]
                self.op += 1
                self.out[self.op] = self.out[self.m_pos + 1]
                self.op += 1
                self.out[self.op] = self.out[self.m_pos + 2]
                self.op += 1

                if self.match_done() == 0:
                    continue
                else:
                    self.match_next()

            ret = self.match()
            if ret != self.OK:
                return self.OK if ret == self.EOF_FOUND else ret

        return self.OK

    def _compressCore(self, in_len, ti):
        ip_start = self.ip
        ip_end = self.ip + in_len - 20
        ii = self.ip

        if ti < 4:
            self.ip += (4 - ti)

        self.ip += 1 + ((self.ip - ii) >> 5)

        while self.ip < ip_end:
            # Build a 32-bit value from 4 bytes in little-endian order.
            dv_lo = self.buf[self.ip] | (self.buf[self.ip + 1] << 8)
            dv_hi = self.buf[self.ip + 2] | (self.buf[self.ip + 3] << 8)
            dindex = ((((dv_lo * 0x429d) >> 16) + (dv_hi * 0x429d) + (dv_lo * 0x1824)) & 0xFFFF) >> 2

            m_pos = ip_start + self.dict[dindex]
            self.dict[dindex] = self.ip - ip_start

            candidate = (self.buf[m_pos] | (self.buf[m_pos + 1] << 8) |
                         (self.buf[m_pos + 2] << 16) | (self.buf[m_pos + 3] << 24))
            current = (self.buf[self.ip] | (self.buf[self.ip + 1] << 8) |
                       (self.buf[self.ip + 2] << 16) | (self.buf[self.ip + 3] << 24))
            if current != candidate:
                self.ip += 1 + ((self.ip - ii) >> 5)
                continue

            ii -= ti
            ti = 0
            t = self.ip - ii

            if t != 0:
                if t <= 3:
                    self.out[self.op - 2] |= t
                    while t > 0:
                        self.out[self.op] = self.buf[ii]
                        self.op += 1
                        ii += 1
                        t -= 1
                else:
                    if t <= 18:
                        self.out[self.op] = t - 3
                        self.op += 1
                    else:
                        tt = t - 18
                        self.out[self.op] = 0
                        self.op += 1
                        while tt > 255:
                            tt -= 255
                            self.out[self.op] = 0
                            self.op += 1
                        self.out[self.op] = tt
                        self.op += 1
                    while t > 0:
                        self.out[self.op] = self.buf[ii]
                        self.op += 1
                        ii += 1
                        t -= 1

            m_len = 4
            if self.buf[self.ip + m_len] == self.buf[m_pos + m_len]:
                while True:
                    m_len += 1
                    if self.buf[self.ip + m_len] != self.buf[m_pos + m_len]:
                        break
                    m_len += 1
                    if self.buf[self.ip + m_len] != self.buf[m_pos + m_len]:
                        break
                    m_len += 1
                    if self.buf[self.ip + m_len] != self.buf[m_pos + m_len]:
                        break
                    m_len += 1
                    if self.buf[self.ip + m_len] != self.buf[m_pos + m_len]:
                        break
                    m_len += 1
                    if self.buf[self.ip + m_len] != self.buf[m_pos + m_len]:
                        break
                    m_len += 1
                    if self.buf[self.ip + m_len] != self.buf[m_pos + m_len]:
                        break
                    m_len += 1
                    if self.buf[self.ip + m_len] != self.buf[m_pos + m_len]:
                        break
                    m_len += 1
                    if self.buf[self.ip + m_len] != self.buf[m_pos + m_len]:
                        break
                    if self.ip + m_len >= ip_end:
                        break

            m_off = self.ip - m_pos
            self.ip += m_len
            ii = self.ip
            if m_len <= 8 and m_off <= 0x0800:
                m_off -= 1
                self.out[self.op] = ((m_len - 1) << 5) | ((m_off & 7) << 2)
                self.op += 1
                self.out[self.op] = m_off >> 3
                self.op += 1
            elif m_off <= 0x4000:
                m_off -= 1
                if m_len <= 33:
                    self.out[self.op] = 32 | (m_len - 2)
                    self.op += 1
                else:
                    m_len -= 33
                    self.out[self.op] = 32
                    self.op += 1
                    while m_len > 255:
                        m_len -= 255
                        self.out[self.op] = 0
                        self.op += 1
                    self.out[self.op] = m_len
                    self.op += 1
                self.out[self.op] = m_off << 2
                self.op += 1
                self.out[self.op] = m_off >> 6
                self.op += 1
            else:
                m_off -= 0x4000
                if m_len <= 9:
                    self.out[self.op] = 16 | ((m_off >> 11) & 8) | (m_len - 2)
                    self.op += 1
                else:
                    m_len -= 9
                    self.out[self.op] = 16 | ((m_off >> 11) & 8)
                    self.op += 1
                    while m_len > 255:
                        m_len -= 255
                        self.out[self.op] = 0
                        self.op += 1
                    self.out[self.op] = m_len
                    self.op += 1
                self.out[self.op] = m_off << 2
                self.op += 1
                self.out[self.op] = m_off >> 6
                self.op += 1

        return in_len - ((ii - ip_start) - ti)

    def compress(self, state):
        self.state = state
        self.ip = 0
        self.buf = bytearray(state['inputBuffer'])
        in_len = len(self.buf)
        max_len = in_len + math.ceil(in_len / 16) + 64 + 3
        state['outputBuffer'] = bytearray(max_len)
        self.out = state['outputBuffer']
        self.op = 0
        self.dict = [0] * 16384
        l = in_len
        t = 0

        while l > 20:
            ll = l if l <= 49152 else 49152
            if ((t + ll) >> 5) <= 0:
                break

            self.dict = [0] * 16384
            prev_ip = self.ip
            t = self._compressCore(ll, t)
            self.ip = prev_ip + ll
            l -= ll

        t += l
        if t > 0:
            ii = in_len - t
            if self.op == 0 and t <= 238:
                self.out[self.op] = 17 + t
                self.op += 1
            elif t <= 3:
                self.out[self.op - 2] |= t
            elif t <= 18:
                self.out[self.op] = t - 3
                self.op += 1
            else:
                tt = t - 18
                self.out[self.op] = 0
                self.op += 1
                while tt > 255:
                    tt -= 255
                    self.out[self.op] = 0
                    self.op += 1
                self.out[self.op] = tt
                self.op += 1
            while t > 0:
                self.out[self.op] = self.buf[ii]
                self.op += 1
                ii += 1
                t -= 1

        self.out[self.op] = 17
        self.op += 1
        self.out[self.op] = 0
        self.op += 1
        self.out[self.op] = 0
        self.op += 1

        state['outputBuffer'] = self.out[:self.op]
        return self.OK