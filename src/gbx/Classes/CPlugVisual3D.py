"""CPlugVisual3D 0902C"""


def Chunk002(bp):
    u0 = bp.uint32("u0")
    
def Chunk004(bp):
    from .CPlugVisual import VERTEX_COUNT, FLAGS
    bit5 =  FLAGS & (1<<5)
    bit6 =  FLAGS & (1<<6)
    
    for i in range(VERTEX_COUNT):
        pos = bp.vec3(f"pos {i}")
        if bit5:
            data5 = bp.uint32(f"data5 {i}")
        if bit6:
            data6 = bp.uint32(f"data6 {i}")
            
    num_tangents_u = bp.uint32("numTangentsU")
    for i in range(num_tangents_u):
        u0 = bp.uint32(f"u0 {i}")
        
    num_tangents_v = bp.uint32("numTangentsV")
    for i in range(num_tangents_v):
        u1 = bp.uint32(f"u1 {i}")
    
    