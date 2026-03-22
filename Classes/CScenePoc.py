"""CScenePoc 0A009"""


def Chunk000(bp):
    is_active = bp.bool("isActive")
    id = bp.nodeId("id")  # FIXME
    u1 = bp.directNodeRef("u1")