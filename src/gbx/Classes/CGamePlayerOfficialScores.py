"""CGamePlayerOfficialScores 03095"""


def Chunk001(bp):
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")
    u3 = bp.uint32("u3")
    u4 = bp.uint32("u4")
    u5 = bp.uint32("u5")
    u6 = bp.uint32("u6")
    u7 = bp.bytes(11, name="u7")
    numZones = bp.uint32("numZones")
    for i in range(numZones):
        zoneName = bp.string(f"zoneName {i}")
        ui = bp.uint32(f"u1 {i}")
        bp.nodeRef(f"highScore {i}")