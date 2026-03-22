"""CGameCtnMediaBlockCameraGame"""

def Chunk001(bp):
    bp.uint32("u1")
    bp.uint32("u2")
    bp.uint32("u3")
    bp.uint32("u4")

def Chunk003(bp):
    bp.float("timeClipStart")
    bp.float("timeClipEnd")
    bp.lookbackString("cameraView")
    bp.uint32("idxTargetPlayer")
