from . import GameIDs
from .Containers import Chunk, Node

class Gbx:
    def __init__(self):
        self.id : GameIDs.NodeId = GameIDs.NodeId.Unassigned
        self.header_chunk_list = []
        self.main_node : Node = Node()
        self.raw_data : bytes
        self.folders : list[str] = []
        self.is_repeat: bool = False  # For consistency with Node class

    def __repr__(self):
        f = f" Gbx : {self.id}\n\n"

        if self.folders:
            f += "Folders: \n"
            for fold in self.folders:
                f += f" - {fold}\n"
        
        if self.header_chunk_list:
            f += "Header chunks : \n\n"
            for chunk in self.header_chunk_list:
                f += str(chunk) + "\n"

        f += str(self.main_node)

        return f

    def __sub__(self, other):
        g = Gbx()
        g.id = self.id #if (self.id == other.id) else (self.id, other.id)
        for i in range(len(self.header_chunk_list)):
            g.header_chunk_list.append(
                self.header_chunk_list[i] - other.header_chunk_list[i]
            )
        g.main_node = self.main_node - other.main_node
        return g  # FIXME WTF IS THAT

    def __getitem__(self, key):
        res = []
        if isinstance(key, GameIDs.ChunkId):
            for chunk in self.header_chunk_list:
                if chunk.id == key:
                    res.append(chunk)
                res.extend(chunk[key])
            res.extend(self.main_node[key])
        elif isinstance(key, GameIDs.NodeId):
            if self.main_node.id == key:
                res.append(self.main_node)
            for chunk in self.header_chunk_list:
                res.extend(chunk[key])
            res.extend(self.main_node[key])
        else:
            raise Exception(f"Unsupported type {type(key)}")
        return res
