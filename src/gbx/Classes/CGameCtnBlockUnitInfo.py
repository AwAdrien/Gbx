"""CGameCtnBlockUnitInfo 24006"""


def Chunk000(bp):
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")

    offset_x = bp.uint32("offsetX")
    offset_y = bp.uint32("offsetY")
    offset_z = bp.uint32("offsetZ")

    clip_num = bp.uint32("numClips")
    if clip_num != 4:
        raise Exception(f"File has {clip_num} clips (expected 4)")

    clip1 = bp.nodeRef("clip1")
    clip2 = bp.nodeRef("clip2")
    clip3 = bp.nodeRef("clip3")
    cliP4 = bp.nodeRef("clip4")


def Chunk001(bp):
    u0 = bp.lookbackString("u0")
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")


def Chunk002(bp):
    u0 = bp.uint32("u0")


def Chunk003(bp):
    u0 = bp.uint32("u0")
    u1 = bp.lookbackString("u1")
    u2 = bp.uint32("u2")
    u3 = bp.uint32("u3")


def Chunk004(bp):
    u0 = bp.uint32("u0")


def Chunk005(bp):
    u0 = bp.lookbackString("u0")