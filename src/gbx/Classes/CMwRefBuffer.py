"""CMwRefBuffer 01026"""

from ..GbxReader import GbxReader
import logging

def Chunk000(bp):
    n1 = bp.uint32("n1")
    n2 = bp.bool("n2")
    n3 = bp.uint32("n3")
    numChunks = bp.uint32("numChunks")
    for i in range(numChunks):
        index = bp.uint32(f"index {i}")
        id = bp.chunkId(f"id {i}")
        if isinstance(bp, GbxReader):
            logging.info(f"Reading chunk {id} (pos {bp.header_size + bp.pos})")
            bp.freezeCurrentChunk()
            chunk = bp.readChunk(id)
            bp.unfreezeCurrentChunk()
            bp.current_chunk.data[f"refchunk {i}"] = chunk
        else:
            chunk = bp.current_chunk
            logging.info(f"Writing chunk {id}")
            data = bp.writeChunk(chunk.data[f"refchunk {i}"])
            bp.current_chunk = chunk
            bp.stored_nodes.append(chunk)  # TODO this should be done more properly
            bp.data.extend(data)