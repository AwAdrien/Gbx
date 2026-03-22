"""CSceneObjectLink 0A014"""


def Chunk001(bp):
    has_mobil = bp.bool("u0")
    if has_mobil:
        u1 = bp.nodeRef("u1")
        u2 = bp.uint32("u2")
        u3 = bp.uint32("u3")
        u4 = bp.lookbackString("u4")
        u5 = bp.uint32("u5")
    else:
        u1 = bp.nodeRef("u1")
    for i in range(3 * 4):
        bp.float(f"mat {i}")
    bp.uint32("u6")


def Chunk002(bp):
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")


def Chunk003(bp):
    u0 = bp.uint32("u0")
