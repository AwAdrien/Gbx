"""Unlimiter 3F001"""


def Chunk003(bp):
    version = bp.uint8("version")
    assert version == 7
    flags1 = bp.uint16("flags1")
    # assert flags1 == 0
    numAngelscriptModules = bp.uint32("numASModules")
    assert numAngelscriptModules == 1
    flagsAS = bp.uint8("flagsAS")
    assert flagsAS == 3  # Core + Empty
    numParameterSets = bp.uint32("numParameterSets")
    assert numParameterSets == 0
    numTriggerGroups = bp.uint32("numTriggerGroups")
    assert numTriggerGroups == 0
    numBlockGroups = bp.uint32("numBlockGroups")
    assert numBlockGroups == 0
    embeddedBlockCount = bp.uint32("embeddedBlockCount")
    assert embeddedBlockCount == 0    
    numMaterialModelRefs = bp.uint32("numMaterialModelRefs")
    assert numMaterialModelRefs == 0
    replacementTextureFlags = bp.uint8("replacementTextureFlags")
    assert replacementTextureFlags == 0
    numEmbeddedImages = bp.uint32("numEmbeddedImages")
    assert numEmbeddedImages == 0 
    numVehicleIdentifiers = bp.uint32("numVehicleIdentifiers")
    assert numVehicleIdentifiers == 0, numVehicleIdentifiers
    
    numBlocks = bp.uint32("numBlocks")
    for i in range(numBlocks):
        # print(bp.current_chunk)
        blockType = bp.uint8(f"blockType {i}")
        assert blockType == 0, blockType  # Game block type
        bn = bp.lookbackString(f"id {i}")
        bp.lookbackString(f"collectionId {i}")
        bp.uint32(f"x {i}")
        bp.uint32(f"y {i}")
        bp.uint32(f"z {i}")
        bp.uint8(f"direction {i}")
        flags2 = bp.uint32(f"flags2 {i}")
        if flags2 & (1<<15):
            bp.lookbackString(f"author {i}")
            bp.nodeRef(f"skin {i}")
        bp.uint16(f"flags3 {i}")