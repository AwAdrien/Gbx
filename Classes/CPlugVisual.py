"""CPlugVisual 09006"""

VERTEX_COUNT = -1
FLAGS = -1


def Chunk001(bp):
    u0 = bp.uint32("u0")


def Chunk004(bp):
    u0 = bp.uint32("u0")


def Chunk005(bp):
    u0 = bp.uint32("u0")
    for i in range(u0):
        u1 = bp.uint32("u1")
        u2 = bp.uint32("u2")
        u3 = bp.uint32("u3")


def Chunk009(bp):
    u0 = bp.uint32("u0")


def Chunk00B(bp):
    u0 = bp.uint32("u0")


def Chunk00E(bp):
    flags = bp.uint32("flags")
    dimension = bp.uint32("dimension")
    num_vertices = bp.uint32("numVertices")
    global VERTEX_COUNT, FLAGS
    VERTEX_COUNT = num_vertices
    FLAGS = flags
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")

    num_points = num_vertices * dimension
    for i in range(dimension - 1):
        d = bp.float(f"d{i}")  # Idk why

    for i in range(num_points):
        p = bp.vec2(f"point {i}")

    bb_max = bp.vec3("boundingBoxMax")
    bb_min = bp.vec3("boundingBoxMin")

    if dimension:
        u7 = bp.uint32("u7")
