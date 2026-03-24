"""CPlugMaterial 09079"""


def Chunk001(bp):
    u0 = bp.nodeRef("u0")


def Chunk007(bp):
    u0 = bp.nodeRef("u0")


def Chunk00D(bp):
    u0 = bp.int32("u0")
    if u0 == -1:
        u1 = bp.uint32("u1")
        u2 = bp.uint32("u2")
        u3 = bp.uint32("u3")
        u4 = bp.nodeRef("u4")
        u5 = bp.uint32("u5")
        u6 = bp.uint32("u6")
        u7 = bp.uint32("u7")


def Chunk00E(bp):
    u0 = bp.uint16("u0")
    u1 = bp.uint16("u1")


def Chunk00F(bp):
    u0 = bp.uint32("u0")
