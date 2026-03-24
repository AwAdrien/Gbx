"""CGameCtnCollectorList 0301B"""

def Chunk000(bp):
    archiveCount = bp.uint32("archiveCount")
    for i in range(archiveCount):
        bp.lookbackString(f"blockName {i}")
        bp.lookbackString(f"collection {i}")
        bp.lookbackString(f"author {i}")
        bp.uint32(f"numPieces {i}")
