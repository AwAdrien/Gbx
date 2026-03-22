"""CPlugSurface 0900C"""


from zmq import has


def Chunk000(bp):
    surfaceGeometry = bp.nodeRef("surfaceGeometry")
    num_materials = bp.uint32("numMaterials")
    for i in range(num_materials):
        has_file = bp.uint32(f"hasFile {i}")
        if has_file:
            node = bp.nodeRef(f"material {i}")
        else:
            id = bp.uint16(f"surfaceID {i}")