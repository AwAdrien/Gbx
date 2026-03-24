"""CPlugVisualIndexed 0906A"""

from ..GameIDs import ChunkId
from ..GbxReader import GbxReader
import logging


def Chunk001(bp):
    u0 = bp.uint32("u0")
    i = 0
    while u0:
        id = bp.chunkId(f"id {i}")
        if id == ChunkId.Facade:
            break
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
        i += 1