"""CFuncKeysNatural 05030"""


def Chunk000(bp):
    u0 = bp.uint32("u0")
    for i in range(u0):
        u1 = bp.float(f"u1 {i}")