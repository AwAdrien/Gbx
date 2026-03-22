"""CGameCtnMediaTrack 03078"""


def Chunk001(bp):
    bp.string("trackName")
    bp.uint32("u1")
    numTracks = bp.uint32("numTracks")
    for i in range(numTracks):
        bp.nodeRef(f"mediaBlock {i}")
    bp.uint32("u2")

def Chunk002(bp):
    bp.bool("keepPlaying")

def Chunk003(bp):
    bp.bool("readOnly")

def Chunk004(bp):
    bp.bool("keepPlaying")
    bp.uint32("u1")
