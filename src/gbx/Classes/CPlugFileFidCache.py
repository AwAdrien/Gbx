"""CPlugFileFidCache 09049"""


def Chunk000(bp):
    version = bp.uint32("version")
    crc32 = bp.uint32("crc32")
    trackPath = bp.string("trackPath")
    numFolderDescs = bp.uint32("num")
    for i in range(numFolderDescs):
        numSubFolder = bp.int32(f"numSubFolder {i}")
        folderName = bp.string(f"folderName {i}")
    numFileDescs = bp.uint32("numTracks")
    for i in range(numFileDescs):
        folderIdx = bp.int32(f"folderIdx {i}")
        filename = bp.string(f"filename {i}")
        offset = bp.int32(f"offset {i}")  # Data offset
        u1 = bp.int32(f"u1 {i}")
        u2 = bp.int32(f"u2 {i}")
        u3 = bp.int32(f"u3 {i}")
        nodeId = bp.nodeId(f"id {i}")
        u4 = bp.bytes(8, name=f"u4 {i}")

    u5 = bp.bytes(8*(numFolderDescs+1), name="u5")
    dataLen = bp.uint32("dataLen")
    data = bp.bytes(dataLen, name="cacheData")