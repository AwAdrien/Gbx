"""CPlugTreeVisualMip 09015"""


def Chunk002(bp):
    num = bp.uint32("num")
    for i in range(num):
        key = bp.float(f"key {i}")
        node = bp.nodeRef(f"node {i}")