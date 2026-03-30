import gbx
import pytest
import pathlib


def get_files(folder):
    path = pathlib.Path(f"tests/files{folder}")
    return [str(f) for f in path.rglob("*") if f.is_file()]


TEST_CASES = [
    # pytest.param(file, "Replays", id=f"replay::{file}")
    # for file in get_files("/Replays")
    # ] + [
    pytest.param(file, "Challenges", id=f"challenge::{file}")
    for file in get_files("/Challenges")
]

TMP_FILE = "/tmp/file.gbx"