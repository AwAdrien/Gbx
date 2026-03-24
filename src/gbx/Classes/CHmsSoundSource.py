"""CHmsSoundSource 0600D"""


def Chunk003(bp):
    u0 = bp.float("u0")
    u1 = bp.float("u1")
    u2 = bp.float("u2")
    
def Chunk004(bp):
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")
    
def Chunk005(bp):
    u0 = bp.uint32("u0")
    u1 = bp.float("u1")
    u2 = bp.float("u2")