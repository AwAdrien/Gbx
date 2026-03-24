"""CFuncKeys 05002"""


def Chunk001(bp):
    u0 = bp.uint32("u0")
    for i in range(u0):
        u1 = bp.float(f"u1 {i}")


def Chunk003(bp):
    u0 = bp.uint32("u0")
