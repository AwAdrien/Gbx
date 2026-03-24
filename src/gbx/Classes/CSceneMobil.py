"""CSceneMobil 0A011"""

    
def Chunk003(bp):
    u0 = bp.uint32("u0")
    for i in range(u0):
        u1 = bp.nodeRef(f"u1 {i}")
    
def Chunk005(bp):
    hms_item = bp.directNodeRef("HmsItem")
    
def Chunk006(bp):
    u0 = bp.uint32("u0")
