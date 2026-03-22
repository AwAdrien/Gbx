"""CPlugSurfaceGeom 0900F"""


def Chunk004(bp):
    u0 = bp.lookbackString("u0")
    bb_max = bp.vec3("boundingBoxMax")
    bb_min = bp.vec3("boundingBoxMin")
    type = bp.uint32("type")
    
    match type:
        case 1:  # GmSurfEllipsoid
            u1 = bp.float("u1")
            u2 = bp.float("u2")
            u3 = bp.float("u3")
        case 7:  # GmSurfMesh
            version = bp.uint32("version")
            
            # TODO this is number of points
            num_textures = bp.uint32("numTextures")
            for i in range(num_textures):
                texture = bp.vec3(f"texture {i}")
                
            num_triangles = bp.uint32("numTriangles")
            for i in range(num_triangles):
                u1 = bp.float(f"u1 {i}")
                u2 = bp.float(f"u2 {i}")
                u3 = bp.float(f"u3 {i}")
                u4 = bp.float(f"u4 {i}")
                v1 = bp.uint32(f"v1 {i}")  # Triangle id
                v2 = bp.uint32(f"v2 {i}")  # Triangle id
                v3 = bp.uint32(f"v3 {i}")  # Triangle id
                material_id = bp.uint16(f"materialId {i}")
                u6 = bp.uint16(f"u6 {i}")
            
            # Octree
            version = bp.uint32("version")
            num_nodes = bp.uint32("u8")
            for i in range(num_nodes):
                num_sub_nodes = bp.uint32(f"numSubNodes {i}")  # TODO are we sure, why is it 1 except for roots
                bbox_max = bp.vec3(f"boundingBoxMax {i}")
                bbox_min = bp.vec3(f"boundingBoxMin {i}")
                parent = bp.int32(f"parent {i}")
        case _:
            import logging
            logging.error(f"Unsupported Geometry {type}")
    uu = bp.uint16("uu")
