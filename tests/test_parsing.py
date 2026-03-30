import gbx
import pytest

from test_general import TEST_CASES


@pytest.mark.parametrize("file,group", TEST_CASES)
def test_parse(file, group):
    gbx.GbxReader(file).readAll()