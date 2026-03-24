import gbx

print(gbx.__file__)

def test_A01():
    
    data = gbx.GbxReader("tests/files/A01-Race.Challenge.Gbx").readAll()
    assert(len(data[gbx.GameIDs.ChunkId.CGameCtnChallenge028]) == 1)

test_A01()