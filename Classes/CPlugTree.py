"""CPlugTree 0904F"""


def Chunk006(bp):
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")
    for i in range(u1):
        bp.nodeRef(f"u2 {i}")
    
def Chunk00D(bp):
    u0 = bp.lookbackString("u0")
    u1 = bp.lookbackString("u1")
    
def Chunk011(bp):
    u0 = bp.nodeRef("u0")
    
def Chunk016(bp):
    u0 = bp.nodeRef("u0")
    u1 = bp.nodeRef("u1")   
    u2 = bp.nodeRef("u2")
    u3 = bp.nodeRef("u3")
    
def Chunk01A(bp):
    flags = bp.uint32("flags")
    if flags & 4:
        for i in range(12):
            bp.float(f"mat {i}") # TODO: Iso4