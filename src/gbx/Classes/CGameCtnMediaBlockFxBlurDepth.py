"""CGameCtnMediaBlockFxBlurDepth 03081"""


def Chunk001(bp):
    numKeys = bp.uint32("numKeys")
    for i in range(numKeys):
        bp.float(f"timeStamp {i}")
        bp.float(f"lensSize {i}")
        bp.bool(f"forceFocus {i}")
        bp.float(f"focusZ {i}")
