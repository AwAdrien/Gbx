# Expose submodules as package attributes
from . import Containers, GameIDs

# Expose main classes/objects at package level
from .Gbx import Gbx
from .GbxReader import GbxReader
from .GbxWriter import GbxWriter

__all__ = [
    "Containers",
    "GameIDs",
    "Gbx",
    "GbxReader",
    "GbxWriter",
]