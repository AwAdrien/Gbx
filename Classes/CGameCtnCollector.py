"""CGameCtnCollector 2E001"""


def Chunk003(bp):
    name = bp.lookbackString("name")
    environement = bp.lookbackString("environement")
    author = bp.lookbackString("author")
    u4 = bp.uint32("u4")
    u5 = bp.string("path")  # ?
    u6 = bp.int32("u6")
    u7 = bp.int32("u7")
    u8 = bp.uint32("u8")
    u9 = bp.uint8("u9")
    u10 = bp.uint32("u10")
    u11 = bp.uint32("u11")


def Chunk004(bp):
    size_x = bp.uint16("sizeX")
    size_y = bp.uint16("sizeY")
    for i in range(size_x):
        bp.bytes(size_y * 4, name=f"row {i}")
        
def Chunk006(bp):
    u0  =bp.uint32("u0")
    
def Chunk007(bp):
    u0 = bp.uint32("u0")
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")
    u3 = bp.uint32("u3")
    u4 = bp.uint32("u4")
    u5 = bp.uint32("u5")
    
def Chunk009(bp):
    u0 = bp.string("u0")
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")
    
def Chunk00A(bp):
    u0 = bp.uint32("u0")
    
def Chunk00B(bp):
    u1 = bp.lookbackString("u1")
    u2 = bp.lookbackString("u2")
    u3 = bp.lookbackString("u3")