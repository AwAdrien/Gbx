import gbx
import pytest
import Levenshtein
import binascii
import logging

from test_general import TEST_CASES, TMP_FILE



def align_sequences(data1, data2):
    """Aligns sequences to handle offsets before comparing."""
    aligned1, aligned2 = [], []

    for tag, i1, i2, j1, j2 in Levenshtein.opcodes(data1, data2):
        if tag == "equal":
            aligned1.extend(data1[i1:i2])
            aligned2.extend(data2[j1:j2])
        elif tag == "replace":
            aligned1.extend(data1[i1:i2])
            aligned2.extend(data2[j1:j2])
        elif tag == "delete":
            aligned1.extend(data1[i1:i2])
            aligned2.extend(b" " * (i2 - i1))
        elif tag == "insert":
            aligned1.extend(b" " * (j2 - j1))
            aligned2.extend(data2[j1:j2])

    return bytes(aligned1), bytes(aligned2)


def format_readable(row: bytes) -> str:
    s: str = ""
    for b in row:
        if 32 <= b <= 126:
            s += chr(b)
        elif b == 20:
            s += " "
        else:
            s += "."
    return s


def compare(data1, data2) -> float:
    """Compares two byte sequences while compensating for shifts."""

    data1, data2 = align_sequences(data1, data2)

    ratio: float = float(f"{Levenshtein.ratio(data1, data2):.4f}")
    print(f"Match: {ratio * 100:.2f}%")

    data_end: int = min(len(data1), len(data2))
    last_error = -999
    window_size = 30

    prints = 0
    for i in range(data_end):
        if (
            data1[i] != data2[i]
            and i - last_error > window_size
            and not (
                data1[i] == 64 and data2[i] == 128
            )  # Lookbackstring flags don't matter and are unpredictable
            and not (data1[i] == 128 and data2[i] == 64)
            and prints < 10
        ):
            prints += 1
            print(
                f"""
byte {i}
{binascii.hexlify(data1[max(0, i-window_size):min(i+window_size, len(data1))])} {format_readable(data1[max(0, i-window_size):min(i+window_size, len(data1))])}
{binascii.hexlify(data2[max(0, i-window_size):min(i+window_size, len(data2))])} {format_readable(data2[max(0, i-window_size):min(i+window_size, len(data2))])}
  {''.join('..' if data1[j] != data2[j] else '  ' for j in range(max(0, i - window_size), min(i+window_size, data_end)))}
"""
            )
            last_error: int = i

    return 1.0 if last_error == -999 else ratio


@pytest.mark.parametrize("file,group", TEST_CASES)
def test_similarity(caplog, file, group):
    caplog.set_level(logging.INFO)
    reader = gbx.GbxReader(file)
    data = reader.readAll()
    writer = gbx.GbxWriter()
    writer.writeAll(data)
    writer.saveToFile(TMP_FILE)

    reader2 = gbx.GbxReader(TMP_FILE)
    data2 = reader2.readAll() #stop_after_decompression=True)
    writer2 = gbx.GbxWriter()
    writer2.writeAll(data2)
    writer2.saveToFile(TMP_FILE)

    reader3 = gbx.GbxReader(TMP_FILE)
    data3 = reader3.readAll()

    for d in data2[gbx.GameIDs.ChunkId.CGameCtnReplayRecord002]:
        print(str(d)[:1000])
    for d in data[gbx.GameIDs.ChunkId.CGameCtnReplayRecord002]:
        print(str(d)[:1000])

    assert(compare(data3.raw_data, data2.raw_data) > 0.99)