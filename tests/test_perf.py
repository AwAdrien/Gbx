import gbx
import pytest

from test_general import TEST_CASES


@pytest.mark.parametrize("file,group", TEST_CASES)
@pytest.mark.benchmark(max_time=0.1, min_rounds=3)
def test_parse_perf(benchmark, file, group):
    benchmark.group = group
    benchmark(lambda: gbx.GbxReader(file).readAll())