"""CGameCtnReplayRecord 03093"""

import gbx.GbxReader as GbxReader


def Chunk000(bp):
    version = bp.uint32("version")
    if version >= 2:
        bp.lookbackString("trackUID", is_local=False)
        bp.lookbackString("environment")
        bp.lookbackString("author", is_local=False)
        bp.uint32("time")
        bp.string("nickname")
        if version >= 6:
            bp.string("driverLogin")
            if version >= 8:
                bp.byte("u1")
                bp.lookbackString("titleUID")


def Chunk001(bp):
    bp.string("XML")


def Chunk002(bp) -> None:
    GBXSize = bp.uint32("GbxSize")
    data = bp.bytes(GBXSize, name="gbxData")
    if isinstance(bp, GbxReader.GbxReader):
        track_reader = GbxReader.GbxReader(data)
        track: GbxReader.Gbx = track_reader.readAll()
        # bp.current_chunk.data["Track"] = track


def Chunk007(bp):
    bp.uint32("u1")


def Chunk014(bp):
    bp.uint32("version")
    num_ghosts = bp.uint32("numGhosts")
    for i in range(num_ghosts):
        bp.nodeRef(f"ghost {i}")
    bp.bytes(4, name="u1")
    num_extras = bp.uint32("numExtras")
    for i in range(num_extras):
        bp.uint32(f"extra 1 {i}")   
        bp.uint32(f"extra 2 {i}")


def Chunk015(bp):
    bp.nodeRef("clip")
