from hashlib import md5
from .GameIDs import ChunkId, NodeId
from .Containers import Array, Quat, Vector2, Vector3, List, Node, Chunk, File, Color
from .Gbx import Gbx
from .Lzo.Lzo import LZO
from .GameIDs import *


import logging
import os
import struct
import builtins
import math

class GbxReader:
    """
    arg1 : data, can be a path to a file or a simple string of data

    This object is used to read each Gbx datatype (see https://wiki.xaseco.org/wiki/GBX#Primitives for more info)
    It holds some local chunk values, and can therefore add each read values to it's internal memory, if a name is
    provided for it.
    """

    def __init__(self, data: str | bytes) -> None:
        if isinstance(data, str):
            if not os.path.isfile(data):
                raise ValueError(f"File {data} does not exist")
            with open(data, "rb") as f:
                self.data: bytes = f.read()
            self.source = data
        elif isinstance(data, bytes):
            self.data: bytes = data
            self.source = "internal"
        self.pos = 0
        self.header_size: int = 0
        self.gbx: Gbx
        self.frozen_chunks = []
        self.seen_lookback = False
        self.node_index = {}
        self.stored_strings = []
        self.current_chunk = Chunk()

    def bool(self, name=None) -> bool:
        """
        Reads a bool (4 bytes) from the buffer
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the bool that was read
        """
        data = self.uint32()
        val: builtins.bool = data == 1

        if data not in [0, 1]:
            logging.warning(f"Wrong value for bool : {data}")

        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def byte(self, name=None) -> str:
        """
        Reads a byte from the buffer
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the byte that was read, as string
        """
        val = str(self.data[self.pos])
        self.pos += 1
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def customArray(self, length: int, arg_list: list, name=None) -> Array:
        """
        Reads an array from the buffer
        :param length: number of elements in the array
        :param arg_list: in the form of tuples (function, name) to specify the data inside each cell
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the array that was read
        """
        array = Array()
        for _ in range(length):
            d = {}
            for f, el_name in arg_list:
                d[el_name] = f(self)()
            array.add(d)
        if name is not None:
            self.current_chunk.data[name] = array
        return array

    def customList(self, arg_list: list, name=None) -> List:
        """
        Reads a list from the buffer (size then data)
        :param arg_list: in the form of tuples (function, name) to specify the data inside each cell
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the list that was read
        """
        clist = List()
        length = self.uint32()
        for _ in range(length):
            d = {}
            for f, el_name in arg_list:
                d[el_name] = f(self)()
            clist.add(d)
        if name is not None:
            self.current_chunk.data[name] = clist
        return clist

    def chunkId(self, name=None) -> ChunkId:
        """
        Reads a chunkId from the buffer (4 bytes hex)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the chunkId that was read (ChunkId.Unknown if unknown, which can cause problems)
        """
        val = int(self.bytes(4, "I"))

        if val in chunk_id_map:
            val = chunk_id_map[val]

        if not ChunkId.intIsChunkId(val):
            logging.error(f"Unknown chunk {hex(val)}")
            import binascii

            logging.info(
                f"Data: {binascii.hexlify(self.data[self.pos:min(len(self.data), self.pos+50)])}"
            )
            raise Exception(f"Unknown Chunk {hex(val)}")
        chunk_id = ChunkId(val)
        if name is not None:
            self.current_chunk.data[name] = chunk_id
        return chunk_id

    def debug(self):
        import binascii
        import inspect

        caller_frame = inspect.stack()[1]
        filename = caller_frame.filename
        lineno = caller_frame.lineno
        logging.warning(
            f"{' . '*len(self.frozen_chunks)}{filename.split('/')[-1]}:{lineno} - {binascii.hexlify(self.data[self.pos : self.pos + 500])}"
        )

    def color(self, name=None) -> Color:
        """
        Reads a color from the buffer (3 floats)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the color that was read
        """
        c = Color()
        c.r, c.g, c.b = self.float(), self.float(), self.float()

        if name is not None:
            self.current_chunk.data[name] = c
        return c

    def fileRef(self, name=None) -> File:
        """
        Reads a file from the buffer (version, checksum, path, url)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the file that was read
        """
        f = File()
        f.version = int(self.byte())
        if f.version >= 3:
            f.checksum = bytes(self.bytes(32))

        f.path = self.string()
        if f.path and f.version >= 1:
            f.locator_url = self.string()

        if name is not None:
            self.current_chunk.data[name] = f
        return f

    def float(self, name=None) -> float:
        """
        Reads a float (4 bytes)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the float that was read
        """
        val = float(self.bytes(4, "f"))
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def freezeCurrentChunk(self):
        """
        Stores the current chunk context, to read a subnode
        """
        # TODO remove both methods
        self.frozen_chunks.append(self.current_chunk)
        self.current_chunk = Chunk()

    def int16(self, name=None) -> int:
        """
        Reads a signed integer (2 bytes)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: The int16 that was read
        """
        val = int(self.bytes(2, "h"))
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def int32(self, name=None) -> int:
        """
        Reads a signed integer (4 bytes)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: The int32 that was read
        """
        val = int(self.bytes(4, "i"))
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def lookbackString(self, name=None, is_local=True) -> str:
        """
        Reads a string with the lookback format, adding it to the lookback table
        (see https://wiki.xaseco.org/wiki/ManiaPlanet_internals#Id for more details)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the string that was read
        """

        if not self.seen_lookback:
            self.uint32()
        self.seen_lookback = True

        inp: builtins.int = self.uint32()
        b30: builtins.int = (inp >> 30) & 1
        b31: builtins.int = (inp >> 31) & 1
        index: builtins.int = inp & 0x3FFFFFFF

        if not (b30 or b31):
            s = str(inp)
            # logging.info(f"Collection id {s}")
        elif b30 ^ b31:
            # TODO figure out local / non local thing
            if index == 0:
                s: builtins.str = self.string()
                self.stored_strings.append(s)
            else:
                s = self.stored_strings[index - 1]
            # if not is_local:
            #     print(s)
            # if b31 and is_local:
            #     logging.warning(f"String {name} ({s}) should not be marked as local")
            # if b30 and not is_local:
            #     if s not in LocalStrings.local_strings:
            #         logging.warning(f"String {name} ({s}) should be marked as local")
        else:
            s = ""
        if name is not None:
            self.current_chunk.data[name] = s

        # print(f"Read {s}, stored {len(self.stored_strings)} total")
        return s

    def nodeId(self, name=None) -> NodeId:
        """
        Reads a nodeId from the buffer (4 bytes hex)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the nodeId that was read (ChunkId.Unknown if unknown, which can cause problems)
        """
        val = int(self.bytes(4, "I"))

        if val in node_id_map:
            val = node_id_map[val]

        if not NodeId.intIsNodeId(val):
            logging.error(f"Unknown node id {hex(val)}")
            raise Exception(f"Unknown node id {hex(val)}")
        node_id = NodeId(val)
        if name is not None:
            self.current_chunk.data[name] = node_id
        return node_id

    def nodeRef(self, name=None) -> Node:
        """
        Reads a sub-node from the buffer
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the node that was read
        """
        index: builtins.int = self.int32()
        if index >= 0 and index not in self.node_index:
            id: NodeId = self.nodeId()
            self.freezeCurrentChunk()
            logging.info(
                f"{' . '*len(self.frozen_chunks)}======== Begin NodeRef {index} ========"
            )
            node: Node = self.readNode()
            node.id = id
            self.node_index[index] = node
            logging.info(
                f"{' . '*len(self.frozen_chunks)}======== End   NodeRef {index} ========"
            )
            self.unfreezeCurrentChunk()
        elif index in self.node_index:
            node = self.node_index[index]
            node.is_repeat = True
        else:
            node = Node()

        if name is not None:
            self.current_chunk.data[name] = node
        return node

    def directNodeRef(self, name=None) -> Node:
        """
        Reads a sub-node from the buffer
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the node that was read
        """
        self.freezeCurrentChunk()
        logging.info(
            f"{' . '*len(self.frozen_chunks)}======== Begin NodeRef (direct) ========"
        )
        node: Node = self.readNode()
        node.id = NodeId.Direct
        logging.info(
            f"{' . '*len(self.frozen_chunks)}======== End   NodeRef (direct) ========"
        )
        self.unfreezeCurrentChunk()

        if name is not None:
            self.current_chunk.data[name] = node
        return node

    def bytes(self, num_bytes: int, format_str: str = "", name=None):
        """
        Reads any specified number of bytes from the buffer, with a special format if specified
        :param num_bytes: number of bytes to read
        :param format_str: format of the unpacked data (default are raw bytes)
        (see https://docs.python.org/3/library/struct.html#struct-format-strings for more details)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the data that was read, in the format specified by format_str
        """
        val: bytes = self.data[self.pos : self.pos + num_bytes]
        self.pos += num_bytes
        if format_str != "":
            try:
                val = struct.unpack(format_str, val)[0]
            except Exception as e:
                logging.error(e)
                raise Exception("Unpack error")

        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def readChunk(self, id: ChunkId) -> Chunk:
        """
        Reads a chunk from the buffer (as a Gbx datatype)
        :param id: ChunkId needed to properly parse the chunk
        :return: the chunk that was read
        """
        from . import BlockImporter

        self.current_chunk = Chunk()
        self.current_chunk.id = id
        if BlockImporter.is_known(id):
            BlockImporter.chunkLink[id.value](self)
        else:
            logging.error(f"Chunk {id} not implemented")
            raise Exception("Unimplemnted")
        return self.current_chunk

    def readNode(self) -> Node:
        """
        Reads a node from the buffer
        :return: the node that was read
        """
        node = Node()
        from . import BlockImporter

        while True:
            id: ChunkId = self.chunkId()
            if id == ChunkId.Facade:
                return node
            skip_size = -1
            if self.bytes(4, "I") == int.from_bytes(b"SKIP", "big"):
                if not BlockImporter.is_skippable(id):
                    logging.warning(f"Chunk {id} should be in skippableChunkList!")
                skip_size: builtins.int = self.uint32()
            else:
                self.pos -= 4
            if BlockImporter.is_known(id):
                logging.info(
                    f"{' . '*len(self.frozen_chunks)}Reading chunk {id} (pos {self.header_size + self.pos})"
                )
                chunk: Chunk = self.readChunk(id)
                node.chunk_list.append(chunk)
            elif skip_size != -1:
                chunk = Chunk()
                chunk.id = id
                chunk.skipped = self.bytes(skip_size)
                if "Unlimiter" in id.name:
                    logging.info(f"Skipping chunk {id}")
                else:
                    logging.warning(f"Skipping chunk {id}")
                    import binascii

                    logging.warning(
                        f"Skipped data : {binascii.hexlify(chunk.skipped)[:100]}"
                    )
                node.chunk_list.append(chunk)
            else:
                logging.error(f"Chunk {id} is unimplemented and unskippable")
                raise Exception("Unimplemented chunk")

    def resetLookbackState(self) -> None:
        """
        Resets the lookbackstring state, needed at the beginning of each new header chunk
        """
        self.seen_lookback = False
        self.stored_strings = []

    def skip(self, num_bytes: int) -> None:
        """
        Skips a specified number of bytes in the buffer
        :param num_bytes: number of bytes to skip
        """
        assert num_bytes > 0
        self.pos += num_bytes

    def string(self, name=None) -> str:
        """
        Reads a string from the buffer (size then data)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the string that was read
        """
        str_len: builtins.int = self.uint32()
        try:
            val: builtins.str = self.bytes(str_len, str(str_len) + "s").decode(
                "utf-8", errors="replace"
            )

        except UnicodeDecodeError as e:
            logging.warning(f"Failed to read string: {e}")
            val = ""

        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def uint8(self, name=None) -> int:
        """
        Reads an unsigned integer (1 byte)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: The uint8 that was read
        """
        val = int(self.bytes(1, "B"))
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def int8(self, name=None) -> int:
        """
        Reads an integer (1 byte)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: The int8 that was read
        """
        val = int(self.bytes(1, "b"))
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def uint16(self, name=None) -> int:
        """
        Reads an unsigned integer (2 bytes)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: The uint16 that was read
        """
        val = int(self.bytes(2, "H"))
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def float16(self, name=None) -> builtins.float:
        """
        Reads an float between 0 and 1 (2 bytes)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: The float16 that was read
        """
        val = float(self.uint16() / (1 << 16))  # TODO INT ??
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def vec3_16(self, name=None) -> Vector3:
        """
        Reads a vector3 from the buffer in compressed form
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the vector3 that was read
        """
        axisHeading = self.int16() * math.pi / ((1 << 15) - 1)
        axisPitch = self.int16() * (math.pi / 2) / ((1 << 15) - 1)

        val = Vector3(
            math.cos(axisHeading) * math.cos(axisPitch),
            math.sin(axisHeading) * math.cos(axisPitch),
            math.sin(axisPitch),
        )

        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def vec3_8(self, name=None) -> Vector3:
        """
        Reads a vector3 from the buffer in compressed form
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the vector3 that was read
        """
        axisHeading = self.int8() * math.pi / ((1 << 7) - 1)
        axisPitch = self.int8() * (math.pi / 2) / ((1 << 7) - 1)

        val = Vector3(
            math.cos(axisHeading) * math.cos(axisPitch),
            math.sin(axisHeading) * math.cos(axisPitch),
            math.sin(axisPitch),
        )

        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def quat_small(self, name=None) -> Quat:
        """
        Reads a quaternion from the buffer in compressed form
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the quaternion that was read
        """
        angle = self.int16() * math.pi / ((1 << 16) - 1)
        axis = self.vec3_16()

        val = Quat(
            axis.x * math.sin(angle),
            axis.y * math.sin(angle),
            axis.z * math.sin(angle),
            math.cos(angle),
        )
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def uint32(self, name=None) -> int:
        """
        Reads an unsigned integer (4 bytes)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: The uint32 that was read
        """
        val = int(self.bytes(4, "I"))
        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def unfreezeCurrentChunk(self) -> None:
        """
        Loads back a chunk that was previously frozen, ex after a noderef
        """
        if not self.frozen_chunks:
            logging.warning("No chunks were frozen!")
        self.current_chunk = self.frozen_chunks.pop()

    def vec2(self, name=None) -> Vector2:
        """
        Reads a vector2 from the buffer (float, float)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the vector2 that was read
        """
        val = Vector2(self.float(), self.float())

        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def vec3(self, name=None):
        """
        Reads a vector3 from the buffer (float, float, float)
        :param name: name of the variable if wanted to be saved in memory (default is None)
        :return: the vector3 that was read
        """
        val = Vector3(self.float(), self.float(), self.float())

        if name is not None:
            self.current_chunk.data[name] = val
        return val

    def readHeaderGbx(self):
        """
        Reads the header of the file with which the GbxReader was initialized
        """
        self.version: builtins.int = self.int16()
        self.format = self.byte()
        self.ref_compression = self.byte()
        self.body_compression = self.byte()
        if self.version >= 4:
            self.byte("u2")

        if self.version >= 3:
            self.gbx.id = self.nodeId()

        if self.version >= 6:
            user_data_size: builtins.int = self.uint32()
            if user_data_size:
                entries: List = self.customList(
                    [(lambda x: x.chunkId, "id"), (lambda x: x.uint32, "size")]
                )
                for c in entries:
                    size, id = c["size"], c["id"]

                    from . import BlockImporter

                    if size & 1 << 31 and not BlockImporter.is_skippable(id):
                        logging.warning(f"Chunk id {id} should be in skippable list")

                    self.resetLookbackState()

                    if BlockImporter.is_known(id):
                        logging.info(
                            f"{' . '*len(self.frozen_chunks)}Reading chunk {id} (pos {self.pos})"
                        )
                        self.readChunk(id)
                        self.gbx.header_chunk_list.append(self.current_chunk)
                    else:
                        if "Unlimiter" in id.name:
                            logging.info(f"Skipping chunk {id}")
                        else:
                            logging.warning(f"Skipping chunk {id}")
                            import binascii

                            logging.warning(
                                f"Skipped data : {binascii.hexlify(self.data[self.pos:self.pos+min(size,100)])} ({size} bytes)"
                            )
                        self.skip(size)

    def readFolders(self, current_path=""):
        res = []
        num_sub_folder = self.uint32()
        for i in range(num_sub_folder):
            current_path = current_path + "/" + self.string()
            res.append(current_path)
            res.extend(self.readFolders(current_path))
        return res

    def externalNode(self, folders):
        n = Node()
        n.id = NodeId.External
        flags = self.uint32()
        if (flags & 4) == 0:
            n.external_name = self.string()
        else:
            n.external_name = f"Index {self.uint32()}"
        node_index = self.uint32()
        if self.version >= 5:
            use_file = self.bool()
        if (flags & 4) == 0:
            folder_index = self.uint32()
            n.external_name = folders[folder_index - 1] + "/" + n.external_name
        # TODO properly store it
        self.node_index[node_index] = n

    def readBodyGbx(self, stop_after_decompression: builtins.bool = False):
        """
        Reads the body of the file with which the GbxReader was initialized
        """
        num_nodes: builtins.int = self.uint32()

        num_external_nodes: builtins.int = self.uint32()

        if num_external_nodes > 0:
            ancestor_level = self.uint32()
            self.gbx.folders = self.readFolders()

            for i in range(num_external_nodes):
                external_node = self.externalNode(self.gbx.folders)

        # We exclude the data sizes from the raw_data : it doesn't match
        # because our compression is better than the one in game
        self.gbx.raw_data = self.data
        self.header_size = self.pos
        self.resetLookbackState()

        if int(self.body_compression) == ord("C"):
            data_size: builtins.int = self.uint32()
            comp_data_size: builtins.int = self.uint32()
            comp_data: builtins.bytes = self.bytes(comp_data_size)

            if comp_data_size <= 0:
                return
            logging.info("Decompressing")
            self.data = LZO().decompress(comp_data, data_size)
        else:
            self.data = self.data[self.pos :]

        self.gbx.raw_data += self.data

        if stop_after_decompression:
            return

        self.pos = 0
        node: Node = self.readNode()
        node.id = NodeId.Body
        self.gbx.main_node = node

    def readPak(self):
        self.version = self.uint32("version")
        # key = self.bytes(16, name="key")
        """ 
            resource 9CBC45E5A368A71B42A213B948B2636C
            game B4CDC7EBA9F5C893E830D8FB061FC3B9
            alpine 540E1B123558C6E70B622D347152D727
            speed 7F931C083551AD6F2315B620567E84B8
            rally 28A296A6A7964338D22C6A3BF4076D51
            island 9EA613D008808323DBB1C240D9546B4E
            coast 6AAE08385BFAFAF5886981D06C933CA1
            bay D1AA6C79C9A3D8A9CB3426BABB055B54
            stadium F0415EA5352011E9C76FF5A97C6FD5D6
            patch1 0DAA898700A2AACA26C99F27B8C61809
            
            ["resource"] = "6343BA1A5C9758E4BD5DEC46B74D9C93",
            ["game"] = "4B323814560A376C17CF2704F9E03C46",
            ["alpine"] = "ABF1E4EDCAA73918F49DD2CB8EAD28D8",
            ["speed"] = "806CE3F7CAAE5290DCEA49DFA9817B47",
            ["rally"] = "D75D69595869BCC72DD395C40BF892AE",
            ["island"] = "6159EC2FF77F7CDC244E3DBF26AB94B1",
            ["coast"] = "9551F7C7A405050A77967E2F936CC35E",
            ["bay"] = "2E559386365C275634CBD94544FAA4AB",
            ["stadium"] = "0FBEA15ACADFEE1638900A5683902A29",
            ["patch1"] = "F2557678FF5D5535D93660D84739E7F6",
        """

        # key = bytes.fromhex("0FBEA15ACADFEE1638900A5683902A29")
        key = bytes.fromhex("F0415EA5352011E9C76FF5A97C6FD5D6")
        print(key, len(key))
        import binascii
        from Crypto.Cipher import Blowfish

        iv = self.bytes(8)
        print(f"IV: {binascii.hexlify(iv)}")
        data = self.bytes(256)
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(data)

        print("Decrypted data (hex):", binascii.hexlify(decrypted_data))
        print("Decrypted data (ascii preview):", decrypted_data[:64])

    def readPackList(self):
        version = self.uint8()
        num_packs = self.uint8()
        crc32 = self.uint32()
        salt = self.uint32()

        for _ in range(num_packs):
            flag = self.uint8()
            name_length = self.uint8()
            encrypted_name = self.bytes(name_length)
            encrypted_key_stream = self.bytes(32)

            name_key = md5(b"6611992868945B0B59536FC3226F3FD0" + str(salt).encode()).digest()
            name = bytes([encrypted_name[i] ^ name_key[i % 16] for i in range(name_length)])
            key_string_key = md5(name + str(salt).encode() + b"B97C1205648A66E04F86A1B5D5AF9862").digest()
            key_string = bytes([encrypted_key_stream[i] ^ key_string_key[i % 16] for i in range(32)])
            key = md5(key_string + b"NadeoPak")

            print(f"Pack Name: {name.decode(errors='ignore')}, Key: {key.hexdigest()}")

            
        signature = self.bytes(16)

    def readAll(self, stop_after_decompression: builtins.bool = False) -> Gbx:
        """
        Reads the whole file with which the GbxReader was initialized
        :return: all the data that was read
        """
        self.gbx = Gbx()

        magic: builtins.bytes = self.bytes(3)
        if magic.decode("utf-8") == "GBX":
            logging.info("Gbx file deteceted")
            self.readHeaderGbx()
            self.readBodyGbx(stop_after_decompression)
            return self.gbx
        self.pos -= 3

        magic: builtins.bytes = self.bytes(8)
        if magic.decode("utf-8") == "NadeoPak":
            logging.info("Pak file detected")
            self.readPak()
            return self.gbx
        self.pos -= 8

        logging.warning(f"File {self.source} has unknown format!")
        return self.gbx
