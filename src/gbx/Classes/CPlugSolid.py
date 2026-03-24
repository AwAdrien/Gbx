"""CPlugSolid 09005"""


def Chunk000(bp):
    u0 = bp.uint32("u0")

def Chunk00E(bp):
    u0 = bp.bytes(64, name="u0")

def Chunk010(bp):
    u0 = bp.uint32("u0")
    
def Chunk011(bp):
    u0 = bp.uint32("u0")
    u1 = bp.bool("u1")
    if u1:
        u3 = bp.uint32("u3")
    u2 = bp.nodeRef("u2")

def Chunk012(bp):
    version = bp.uint8("version")