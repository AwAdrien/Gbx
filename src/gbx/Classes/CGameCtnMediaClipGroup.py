"""CGameCtnMediaClipGroup 0307A"""


def Chunk002(bp):
    bp.uint32("u1")
    numClips = bp.uint32("numClips")
    for i in range(numClips):
        bp.nodeRef(f"clip {i}")
    numClips = bp.uint32("numClips")
    for i in range(numClips):
        numCoords = bp.uint32(f"numCoords {i}")
        for j in range(numCoords):
            bp.vec3(f"coords {i} {j}")
        bp.vec3(f"refFramePos {i}")
        bp.uint32(f"refFrameRot {i}")

def Chunk003(bp):
    bp.uint32("u1")
    numClips = bp.uint32("numClips")
    for i in range(numClips):
        bp.nodeRef(f"clip {i}")
    numClips = bp.uint32("numClips")
    for i in range(numClips):
        bp.vec3(f"refFramePos {i}")
        bp.uint32(f"refFrameRot {i}")
        bp.uint32(f"triggerCondition {i}")
        bp.float(f"triggerArgument {i}")
        numTriggers = bp.uint32(f"numTriggers {i}")
        for j in range(numTriggers):
            bp.vec3(f"position {i} {j}")
