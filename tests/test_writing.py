import gbx
import pytest

from test_general import TEST_CASES, TMP_FILE

@pytest.mark.parametrize("file,group", TEST_CASES)
def test_write(file, group):
    data = gbx.GbxReader(file).readAll()
    writer = gbx.GbxWriter()
    writer.writeAll(data)
    writer.saveToFile(TMP_FILE)
    data2 = gbx.GbxReader(TMP_FILE).readAll()