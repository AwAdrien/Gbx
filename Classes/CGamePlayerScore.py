"""CGamePlayerScore 0308D"""


def Chunk004(bp):
    login = bp.string("login")
    displayName = bp.string("displayName")
    playerKey = bp.lookbackString("playerKey")
    numOfficialRecs = bp.uint32("numOfficialRecs")
    numRecs = bp.uint32("numRecs")

    for i in range(numRecs):
        mapUUID = bp.lookbackString(f"mapUUID {i}")
        environment = bp.lookbackString(f"environment {i}")
        author = bp.lookbackString(f"author {i}")
        u1 = bp.bytes(28, name=f"u1 {   i}")
        n0 = bp.uint32(f"n0 {i}")
        u2 = bp.bytes(29, name=f"u2 {i}")

        mapName = bp.string(f"mapName {i}")
        bestScore = bp.int32(f"bestScore {i}")
        bestTime = bp.int32(f"bestTime {i}")
        stuntScore = bp.int32(f"stuntScore {i}")
        numFinishes = bp.int32(f"numFinishes {i}")
        n2 = bp.int32(f"n2 {i}")
        copperScore = bp.int32(f"copperScore {i}")
        u3 = bp.bytes(16, name=f"u3 {i}")

def Chunk006(bp):
    bp.uint32("u1")
    bp.uint32("u2")
    
def Chunk00F(bp):
    bp.nodeRef("officialScore")
    
    num = bp.uint32("num")
    for i in range(num):
        name = bp.lookbackString(f"name {i}")
        u1 = bp.uint32(f"u1 {i}")
        bp.nodeRef(f"officialScore {i}")
        u2 = bp.uint32(f"u2 {i}")
    numCampaignScores = bp.uint32("numcampaignScores")
    for i in range(numCampaignScores):
        bp.nodeRef(f"campaignScore {i}")
    
def Chunk010(bp):
    version = bp.uint8("version")
    num = bp.uint32("num")
    for i in range(num):
        name = bp.lookbackString(f"name {i}")
        n1 = bp.uint32(f"n1 {i}")
        n2 = bp.uint32(f"n2 {i}")
        
def Chunk011(bp):
    u1 = bp.bytes(136, name="u1")
        
def Chunk012(bp):
    u1 = bp.uint32("u1")