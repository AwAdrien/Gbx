"""CMotionPlayer 08034"""

    
def Chunk000(bp):
    pass

def Chunk004(bp):
    base = bp.directNodeRef("base")
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")
    u2 = bp.lookbackString("u2")
    num_tracks = bp.uint32("numTracks")
    for i in range(num_tracks):
        bp.nodeRef(f"track {i}")