"""CPlugGameSkin 090F4"""


def Chunk000(bp):
    version = bp.uint8("version")
    relative_folder = bp.string("relativeFolder")
    u2 = bp.uint32("u2")
    u3 = bp.uint32("u3")
    num_skins = bp.uint8("numSkins")
    for i in range(num_skins):
        id = bp.chunkId(f"id {i}")
        type = bp.string(f"type {i}")
        file_path = bp.string(f"file_path {i}")
        u7 = bp.uint32(f"u7 {i}")
    u8 = bp.uint32(f"u8")

