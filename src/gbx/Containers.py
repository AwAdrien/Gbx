from . import GameIDs

import numpy as np


class Array:
    def __init__(self):
        self.size = 0
        self.data = []

    def add(self, other):
        self.data.append(other)
        self.size += 1

    def __eq__(self, other):
        return self.data == other.data


class Chunk:
    def __init__(self):
        self.id: GameIDs.ChunkId = GameIDs.ChunkId.Unassigned
        self.data = {}
        self.depth = 0
        self.skipped = bytes()

    def __eq__(self, other):
        if not isinstance(other, Chunk):
            return False
        return self.data == other.data and self.id == other.id

    def __repr__(self):
        seen = set()

        def dd(depth: int) -> str:
            s = ""
            for i in range(depth):
                if i & 1:
                    s += "   "
                else:
                    s += "|  "
            return s

        def rprint(cont, depth: int, name: str) -> str:
            s = ""
            if isinstance(cont, Chunk):
                s += dd(depth) + f"{cont.id}: \n"
                for v in cont.data.keys():
                    s += rprint(cont.data[v], depth + 1, name=v)
            elif isinstance(cont, Node):
                if cont.id == GameIDs.NodeId.External:
                    return s + " " + cont.external_name + "\n"
                s += dd(depth) + f"{cont.id} : {name}"
                if cont not in seen:
                    seen.add(cont)
                    s += "\n"
                    for c in cont.chunk_list:
                        s += rprint(c, depth + 1, "")
                else:
                    s += "(already printed)\n"
                s += dd(depth) + "\n"
            else:
                s += dd(depth) + f"{name} : {cont}\n"

            return s

        return rprint(self, 0, "")

    def __getitem__(self, key):
        from .Gbx import Gbx

        if isinstance(key, GameIDs.ChunkId):
            res = []
            for v in self.data.keys():
                if isinstance(self.data[v], (Node, Gbx)): # and not self.data[v].is_repeat:
                    res.extend(self.data[v][key])
            return res
        elif isinstance(key, GameIDs.NodeId):
            res = []
            for v in self.data.keys():
                if isinstance(self.data[v], Node): # and not self.data[v].is_repeat:
                    if self.data[v].id == key:
                        res.append(self.data[v])
            for v in self.data.keys():
                if isinstance(self.data[v], (Node, Gbx)): # and not self.data[v].is_repeat:
                    res.extend(self.data[v][key])
            return res
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __sub__(self, other: "Chunk") -> "Chunk":
        raise Exception("Why are we doing that ??")
        c = Chunk()

        c.id = self.id if (self.id == other.id) else (self.id, other.id)
        for el in self.data:
            if el not in other.data or self.data[el] != other.data[el]:
                c.data[el] = self.data[el]
        return c


class List:
    def __init__(self):
        self.size = 0
        self.data = []

    def add(self, other):
        self.data.append(other)
        self.size += 1

    def __eq__(self, other):
        return self.data == other.data

    def __iter__(self):
        for v in self.data:
            yield v


class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0) -> None:
        self.x: float = x
        self.y: float = y
        self.z: float = z

    def __getitem__(self, key) -> float:
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        raise Exception(f"Out of bound: {key}")

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def norm(self) -> float:
        return np.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def direction(self):
        n = self.norm()
        return [self.x / n, self.y / n, self.z / n]

    def to_list(self) -> list[float]:
        return [self.x, self.y, self.z]


class Quat:
    def __init__(self, x, y, z, w) -> None:
        self.x: float = x
        self.y: float = y
        self.z: float = z
        self.w: float = w

    def __eq__(self, other) -> bool:
        return (
            self.x == other.x
            and self.y == other.y
            and self.z == other.z
            and self.w == other.w
        )

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def to_list(self) -> list[float]:
        return [self.x, self.y, self.z, self.w]

    def to_rotation_matrix(self):
        quat = np.asarray(self.to_list())

        # Normalize the quaternion to be safe
        norm = np.linalg.norm(quat)
        if norm == 0:
            raise ValueError("Zero-length quaternion is invalid for rotation")

        x, y, z, w = quat / norm

        xx, yy, zz = x * x, y * y, z * z
        xy, xz, yz = x * y, x * z, y * z
        wx, wy, wz = w * x, w * y, w * z

        rot_matrix = np.array(
            [
                [1 - 2 * (yy + zz), 2 * (xy - wz), 2 * (xz + wy)],
                [2 * (xy + wz), 1 - 2 * (xx + zz), 2 * (yz - wx)],
                [2 * (xz - wy), 2 * (yz + wx), 1 - 2 * (xx + yy)],
            ]
        )

        return rot_matrix


class Vector2:
    def __init__(self, x, y) -> None:
        self.x: float = x
        self.y: float = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __getitem__(self, key) -> float:
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        raise Exception(f"Out of bound: {key}")

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


class File:
    def __init__(self):
        self.version: int
        self.checksum: bytes
        self.path = ""
        self.locator_url = ""

    def __repr__(self):
        return f"{self.path} {self.locator_url}"


class Color:
    def __init__(self):
        self.r = 0.0
        self.g = 0.0
        self.b = 0.0

    def __repr__(self):
        return f"Color ({self.r}, {self.g}, {self.b})"


class Node:
    def __init__(self):
        self.id: GameIDs.NodeId = GameIDs.NodeId.Empty
        self.chunk_list = []
        self.depth = 0
        self.is_repeat = False  # For noderefs
        self.external_name: str  # For external nodes

    # TODO: This was implemented to use noderef, not super happy with it
    def __eq__(self, other) -> bool:
        return self is other

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:

        seen = set()

        def dd(depth: int) -> str:
            s = ""
            for i in range(depth):
                if i & 1:
                    s += "   "
                else:
                    s += "|  "
            return s

        def rprint(cont, depth: int, name: str = "") -> str:
            s = ""
            if isinstance(cont, Chunk):
                s += dd(depth) + f"{cont.id}: \n"
                for v in cont.data.keys():
                    s += rprint(cont.data[v], depth + 1, name=v)
            elif isinstance(cont, Node):
                s += dd(depth) + "\n" + dd(depth) + f"{cont.id} : {name}"
                if cont.id == GameIDs.NodeId.External:
                    return s + " " + cont.external_name + "\n"
                if cont not in seen:
                    seen.add(cont)
                    s += "\n"
                    for c in cont.chunk_list:
                        s += rprint(c, depth + 1)
                else:
                    s += "(already printed)\n"
            else:
                s += dd(depth) + f"{name} : {cont}\n"
            return s

        return rprint(self, 0)

    def __sub__(self, other):
        # FIXME WHY
        raise Exception("Nuh uh")
        n = Node()

        n.id = self.id  # if (self.id == other.id) else (self.id, other.id)
        for i in range(len(self.chunk_list)):
            n.chunk_list.append(self.chunk_list[i] - other.chunk_list[i])
        return n

    def __getitem__(self, key):
        res = []
        if isinstance(key, GameIDs.ChunkId):
            for chunk in self.chunk_list:
                if chunk.id == key:
                    res.append(chunk)
            for chunk in self.chunk_list:
                res.extend(chunk[key])
        elif isinstance(key, GameIDs.NodeId):
            for chunk in self.chunk_list:
                res.extend(chunk[key])
        else:
            raise Exception(f"Unhandled type {type(key)}")
        return res
