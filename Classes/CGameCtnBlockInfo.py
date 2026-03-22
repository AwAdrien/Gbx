"""CGameCtnBlockInfo 24005"""


def Chunk005(bp):
    name = bp.lookbackString("name")
    u1 = bp.uint32("u1")
    u2 = bp.uint32("u2")
    u3 = bp.uint32("u3")
    is_pillar = bp.uint32("isPillar")
    u5 = bp.uint32("u5")
    u6 = bp.uint32("u6")

    pillar = bp.nodeRef("pillar")

    num_ground_unit_info = bp.uint32("numGroundUnitInfo")
    for i in range(num_ground_unit_info):
        ground_unit_info = bp.nodeRef(f"groundUnitInfo {i}")

    num_air_unit_info = bp.uint32("numAirUnitInfo")
    for i in range(num_air_unit_info):
        air_unit_info = bp.nodeRef(f"airUnitInfo {i}")

    num_ground_mobil_arrays = bp.uint32("numGroundMobilArrays")
    for i in range(num_ground_mobil_arrays):
        num_ground_mobil = bp.uint32(f"numGroundMobil {i}")
        for j in range(num_ground_mobil):
            ground_mobil = bp.nodeRef(f"groundMobil {i} {j}")
            
    num_air_mobil_arrays = bp.uint32("numAirMobilArrays")
    for i in range(num_air_mobil_arrays):
        num_air_mobil = bp.uint32(f"numAirMobil {i}")
        for j in range(num_air_mobil):
            air_mobil = bp.nodeRef(f"airMobil {i} {j}")
    
    u17 = bp.uint8("u17")
    u18 = bp.uint32("u18")
    u19 = bp.uint32("u19")


def Chunk009(bp):
    u0 = bp.uint32("u0")


def Chunk00C(bp):
    for i in range(24):
        u0 = bp.float(f"u0 {i}")
        
def Chunk00D(bp):
    u0 = bp.uint32("u0")
    
def Chunk00E(bp):
    u0 = bp.uint32("u0")

    u1 = bp.nodeRef("u1")
    u2 = bp.nodeRef("u2")
    u3 = bp.nodeRef("u3")
    
def Chunk00F(bp):
    u0 = bp.uint32("u0")