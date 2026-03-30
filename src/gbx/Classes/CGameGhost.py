"""CGameGhost 0303F"""

import zlib
import gbx

SAMPLE_SIZE = 61


def Chunk005(bp):
    if isinstance(bp, gbx.GbxReader):
        readChunk005(bp)
    else:
        writeChunk005(bp)


def readChunk005(bp):
    uncomp_size = bp.uint32("uncompSize")
    comp_size = bp.uint32("compSize")
    comp_data = bp.bytes(comp_size, name="compData")

    data = zlib.decompress(comp_data, 0, uncomp_size)
    gr = gbx.GbxReader(data)
    gr.current_chunk.id = gr.chunkId()  # TODO
    skip_list: bool = gr.bool("skipList")
    gr.uint32("U1")
    gr.uint32("samplePeriod")
    version = gr.uint32("version")
    
    if version != 9:
        import logging
        logging.warning(f"Unsupported sample data version : {version}")
        return

    sample_data_size = gr.uint32("sampleDataSize")
    for i in range(sample_data_size // SAMPLE_SIZE):
        # CHmsStateDyna
        pos = gr.vec3(f"position {i}")
        quat = gr.quat_small(f"quat {i}")
        
        speed_norm = gr.int16(f"speedNorm {i}")
        speed_direction = gr.vec3_8(f"speedDirection {i}")
        
        angular_speed_norm = gr.uint16(f"angularSpeedNorm {i}")
        angular_speed_direction = gr.vec3_8(f"angulatSpeedDirection {i}")
        
        # SVehicleSimpleState_ReplayAfter081205
        speed_forward = gr.float16(f"speedForward {i}")
        speed_sideward = gr.float16(f"speedSideward {i}")
        
        rpm = gr.uint16(f"RPM {i}")
        wr1 = gr.uint16(f"wheelRotFL {i}")
        wr2 = gr.uint16(f"wheelRotFR {i}")
        wr3 = gr.uint16(f"wheelRotRR {i}")
        wr4 = gr.uint16(f"wheelRotRL {i}")
        
        steer = gr.uint8(f"steer {i}")
        gas = gr.uint8(f"gas {i}")
        brake = gr.uint8(f"brake {i}")
        u1 = gr.uint8(f"u1 {i}")
        
        u2 = gr.uint8(f"u2 {i}")
        u3 = gr.uint8(f"u3 {i}")
        u4 = gr.uint8(f"u4 {i}")
        
        turbo = gr.uint8(f"turbo {i}")
        
        steerFront = gr.uint8(f"steerFront {i}")
        
        dampen_len_fl = gr.uint8(f"dampenLenFL {i}")
        material_id_fl = gr.uint8(f"materialIdFL {i}")
        dampen_len_fr = gr.uint8(f"dampenLenFR {i}")
        material_id_fr = gr.uint8(f"materialIdFR {i}")
        dampen_len_rr = gr.uint8(f"dampenLenRR {i}")
        material_id_rr = gr.uint8(f"materialIdRR {i}")
        dampen_len_rl = gr.uint8(f"dampenLenRL {i}")
        material_id_rl = gr.uint8(f"materialIdRL {i}")
        
        # Bunch of flags
        u6 = gr.uint8(f"u6 {i}")  # horn  + turbo ?
        u7 = gr.uint8(f"u7 {i}")  # 
        u8 = gr.uint8(f"u8 {i}")
        u9 = gr.uint8(f"u9 {i}")  # dirt ?
    # gr.skip(sample_data_size)

    num_samples = gr.uint32("numSamples")
    if num_samples > 0:
        gr.uint32("offset")
        if num_samples > 1:
            size_per_sample = gr.int32("sizePerSample")
            if size_per_sample == -1:
                return
            # TODO investigate
            assert (
                size_per_sample == SAMPLE_SIZE
            ), f"Bad size per sample: {size_per_sample}!=61"
            assert size_per_sample * num_samples == sample_data_size
            if size_per_sample == -1:
                sample_sizes = []
                for _ in range(num_samples - 1):
                    sample_sizes.append(gr.uint32())

    if not skip_list:
        # num = bp.uint32("num")
        bp.array(lambda x: x.uint32("time"), "sampleTimes")
    bp.current_chunk.data["sampleData"] = gr.current_chunk


def writeChunk005(bw):
    # TODO allow for modifying maps inside replays ?
    bw.uint32("uncompSize")
    compSize = bw.uint32("compSize")
    bw.bytes(compSize, name="compData")
