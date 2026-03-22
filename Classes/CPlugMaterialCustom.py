"""CPlugMaterialCustom 0903A"""


def Chunk004(bp):
    u0 = bp.uint32("u0")
    for i in range(u0):
        u1 = bp.nodeRef("u1")


def Chunk006(bp):
    u0 = bp.uint32("u0")
    for i in range(u0):
        u1 = bp.lookbackString(f"u2 {i}")
        u2 = bp.uint32(f"u0 {i}")
        u3 = bp.uint32(f"u0 {i}")


def Chunk00A(bp):
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")


def Chunk00C(bp):
    u0 = bp.uint32("u0")
    for i in range(u0):
        u1 = bp.lookbackString(f"u1 {i}")
        u2 = bp.uint32(f"u1 {i}")

def Chunk00D(bp):
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")
    u3 = bp.uint32("u3")
    if u0 & 1:
        u4 = bp.uint16("u4")
        u5 = bp.uint16("u5")
