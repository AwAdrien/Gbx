"""CGameCampaignPlayerScores 030EA"""


def Chunk001(bp):
    s1 = bp.lookbackString("s1")
    u1 = bp.bytes(29, name="u1")
    n1 = bp.uint32("n1")
    for i in range(n1):
        u2 = bp.bytes(7, name= f"u2 {i}")
    u3 = bp.bytes(6, name="u3")