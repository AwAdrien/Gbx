"""CPlugFileIndexBuffer 09057"""


def Chunk000(bp):
    u0 = bp.uint32("u0")
    size = bp.uint32("u1")
    for i in range(size//3):
        u2 = bp.uint16(f"u2 {i}")
        u3 = bp.uint16(f"u3 {i}")
        u4 = bp.uint16(f"u4 {i}")