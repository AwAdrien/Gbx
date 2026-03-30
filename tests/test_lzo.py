import os
import random
import pytest
from gbx.Lzo.Lzo import LZO

def roundtrip(data: bytes):
    compressed = LZO().compress(data)
    decompressed = LZO().decompress(compressed, len(data))
    assert decompressed == data

def test_empty():
    data = b''
    roundtrip(data)

def test_all_byte_values():
    data = bytes(range(256))
    roundtrip(data)

def test_highly_compressible():
    data = b'A' * 4096
    roundtrip(data)

@pytest.mark.parametrize("size", [1, 2, 3, 4, 5, 16, 31, 64, 128, 255, 512, 1023, 2048])
def test_various_sizes(size):
    data = os.urandom(size)
    roundtrip(data)