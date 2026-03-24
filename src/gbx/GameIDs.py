from enum import Enum


class ChunkId(Enum):
    """
    Enum of the supported chunk ids (see https://wiki.xaseco.org/wiki/Class_IDs for more info)
    """

    Unassigned = 0
    Unlimiter000 = 0x3F001000  # TODO Unlimiter
    Unlimiter003 = 0x3F001003
    Idk = 0x27133172
    CControlEffectSimi000 = 0x07010000
    CControlEffectSimi004 = 0x07010004
    CControlEffectSimi005 = 0x07010005
    CFuncPlug005 = 0x0500B005
    CFuncKeys001 = 0x05002001
    CFuncKeys003 = 0x05002003
    CFuncKeysNatural000 = 0x05030000
    CFuncTreeSubVisualSequence001 = 0x05031001
    CFuncTreeSubVisualSequence002 = 0x05031002
    CFuncTreeSubVisualSequence003 = 0x05031003
    CGameCampaignPlayerScores001 = 0x030EA001
    CGameCtnBlockSkin000 = 0x3059000
    CGameCtnBlockSkin002 = 0x3059002
    CGameCtnBlockSkin003 = 0x3059003
    CGameCtnBlockInfoFlat001 = 50655233
    CGameCtnBlockInfoClip002 = 0x24024002
    CGameCtnBlockInfoRoad000 = 0x24023000
    CGameCtnChallenge000 = 0x03043000
    CGameCtnChallenge002 = 0x03043002
    CGameCtnChallenge003 = 0x03043003
    CGameCtnChallenge004 = 0x03043004
    CGameCtnChallenge005 = 0x03043005
    CGameCtnChallenge006 = 0x03043006
    CGameCtnChallenge007 = 0x03043007
    CGameCtnChallenge008 = 0x03043008
    CGameCtnChallenge00D = 0x0304300D
    CGameCtnChallenge011 = 0x03043011
    CGameCtnChallenge014 = 0x03043014
    CGameCtnChallenge016 = 0x03043016
    CGameCtnChallenge017 = 0x03043017
    CGameCtnChallenge018 = 0x03043018
    CGameCtnChallenge019 = 0x03043019
    CGameCtnChallenge01C = 0x0304301C
    CGameCtnChallenge01F = 0x0304301F
    CGameCtnChallenge021 = 0x03043021
    CGameCtnChallenge022 = 0x03043022
    CGameCtnChallenge024 = 0x03043024
    CGameCtnChallenge025 = 0x03043025
    CGameCtnChallenge026 = 0x03043026
    CGameCtnChallenge028 = 0x03043028
    CGameCtnChallenge029 = 0x03043029
    CGameCtnChallenge02A = 0x0304302A
    CGameCtnChallengeParameters000 = 0x0305B000
    CGameCtnChallengeParameters001 = 0x0305B001
    CGameCtnChallengeParameters004 = 0x0305B004
    CGameCtnChallengeParameters005 = 0x0305B005
    CGameCtnChallengeParameters006 = 0x0305B006
    CGameCtnChallengeParameters008 = 0x0305B008
    CGameCtnCollectorList000 = 50442240
    CGameCtnCollector003 = 0x2E001003
    CGameCtnCollector004 = 0x2E001004
    CGameCtnCollector005 = 0x2E001005
    CGameCtnCollector006 = 0x0301A006
    CGameCtnCollector007 = 0x0301A007
    CGameCtnCollector009 = 0x0301A009
    CGameCtnCollector00A = 0x0301A00A
    CGameCtnCollector00B = 0x0301A00B
    CGameCtnGhost000 = 50929664
    CGameCtnGhost005 = 50929669
    CGameCtnGhost008 = 50929672
    CGameCtnGhost009 = 50929673
    CGameCtnGhost00A = 50929674
    CGameCtnGhost00B = 50929675
    CGameCtnGhost00C = 50929676
    CGameCtnGhost00E = 50929678
    CGameCtnGhost00F = 50929679
    CGameCtnGhost010 = 50929680
    CGameCtnGhost012 = 50929682
    CGameCtnGhost013 = 50929683
    CGameCtnGhost014 = 50929684
    CGameCtnGhost015 = 50929685
    CGameCtnGhost017 = 50929687
    CGameCtnGhost018 = 50929688
    CGameCtnGhost019 = 50929689
    CGameCtnMediaBlockCameraCustom000 = 0x030A2000
    CGameCtnMediaBlockCameraCustom002 = 0x030A2002
    CGameCtnMediaBlockCameraCustom005 = 0x030A2005
    CGameCtnMediaBlockCameraEffectShake000 = 51003392
    CGameCtnMediaBlockCameraGame000 = 0x03084000
    CGameCtnMediaBlockCameraGame001 = 0x03084001
    CGameCtnMediaBlockCameraGame003 = 0x03084003
    CGameCtnMediaBlockCameraPath000 = 0x030A1000
    CGameCtnMediaBlockCameraPath002 = 0x030A1002
    CGameCtnMediaBlockFxBloom001 = 0x03083001
    CGameCtnMediaBlockFxBlurMotion000 = 50864128
    CGameCtnMediaBlockFxBlurDepth001 = 0x03081001
    CGameCtnMediaBlockFxColors003 = 0x03080003
    CGameCtnMediaBlockGhost001 = 51269633
    CGameCtnMediaBlockGhost002 = 51269634
    CGameCtnMediaBlockMusicEffect000 = 0x30A6000
    CGameCtnMediaBlockMusicEffect001 = 0x30A6001
    CGameCtnMediaBlockImage000 = 0x030A5000
    CGameCtnMediaBlockSound001 = 0x030A7001
    CGameCtnMediaBlockSound002 = 0x030A7002
    CGameCtnMediaBlockSound003 = 0x030A7003
    CGameCtnMediaBlockSound004 = 0x030A7004
    CGameCtnMediaBlockText000 = 51019776
    CGameCtnMediaBlockText001 = 51019777
    CGameCtnMediaBlockText002 = 51019778
    CGameCtnMediaBlockTime000 = 50876416
    CGameCtnMediaBlockTrails000 = 51023872
    CGameCtnMediaBlockTransitionFade000 = 51032064
    CGameCtnMediaBlockTriangles001 = 50499585
    CGameCtnMediaBlockUi001 = 0x0307D001
    CGameCtnMediaClip000 = 0x03079000
    CGameCtnMediaClip003 = 0x03079003
    CGameCtnMediaClip004 = 0x03079004
    CGameCtnMediaClip005 = 0x03079005
    CGameCtnMediaClip007 = 0x03079007
    CGameCtnMediaClipGroup000 = 0x0307A000
    CGameCtnMediaClipGroup002 = 0x0307A002
    CGameCtnMediaClipGroup003 = 0x0307A003
    CGameCtnMediaTrack000 = 0x03078000
    CGameCtnMediaTrack001 = 0x03078001
    CGameCtnMediaTrack002 = 0x03078002
    CGameCtnMediaTrack003 = 0x03078003
    CGameCtnMediaTrack004 = 0x03078004
    CGameCtnReplayRecord000 = 50933760
    CGameCtnReplayRecord001 = 50933761
    CGameCtnReplayRecord002 = 50933762
    CGameCtnReplayRecord007 = 50933767
    CGameCtnReplayRecord014 = 50933780
    CGameCtnReplayRecord015 = 50933781
    CGameHighScore002 = 0x3047002
    CGameGhost005 = 50589701
    CGamePlayerOfficialScores001 = 0x03095001
    CGamePlayerScore004 = 0x0308D004
    CGamePlayerScore006 = 0x0308D006
    CGamePlayerScore00F = 0x0308D00F
    CGamePlayerScore010 = 0x0308D010
    CGamePlayerScore011 = 0x0308D011
    CGamePlayerScore012 = 0x0308D012
    CHmsItem001 = 0x06003001
    CHmsItem011 = 0x06003011
    CHmsSoundSource003 = 0x0600D003
    CHmsSoundSource004 = 0x0600D004
    CHmsSoundSource005 = 0x0600D005
    CMotion000 = 0x08001000
    CMotionCmdBase002 = 0x08029002
    CMotionPlayer000 = 0x08034000
    CMotionPlayer004 = 0x08034004
    CMotionShader000 = 0x0802B000
    CMwRefBuffer000 = 0x01026000
    CPlugIndexBuffer000 = 0x09057000
    CPlugFileImg = 0x09025000
    CPlugFileFidCache000 = 0x09049000
    CPlugGameSkin000 = 0x090F4000
    CPlugMaterial001 = 0x09079001
    CPlugMaterial007 = 0x09079007
    CPlugMaterial00D = 0x0907900D
    CPlugMaterial00E = 0x0907900E
    CPlugMaterial00F = 0x0907900F
    CPlugMaterialCustom004 = 0x0903A004
    CPlugMaterialCustom006 = 0x0903A006
    CPlugMaterialCustom00A = 0x0903A00A
    CPlugMaterialCustom00C = 0x0903A00C
    CPlugMaterialCustom00D = 0x0903A00D
    CPlugShader00E = 0x0900200E
    CPlugShader016 = 0x09002016
    CPlugShaderApply002 = 0x09026002
    CPlugShaderApply004 = 0x09026004
    CPlugShaderApply008 = 0x09026008
    CPlugShaderGeneric003 = 0x09004003
    CPlugSolid000 = 0x09005000
    CPlugSolid00E = 0x0900500E
    CPlugSolid010 = 0x09005010
    CPlugSolid011 = 0x09005011
    CPlugSolid012 = 0x09005012
    CPlugSurface000 = 0x0900C000
    CPlugSurfaceGeom004 = 0x0900F004
    CPlugTree006 = 0x0904F006
    CPlugTree00D = 0x0904F00D
    CPlugTree011 = 0x0904F011
    CPlugTree016 = 0x0904F016
    CPlugTree01A = 0x0904F01A
    CPlugTreeLight004 = 0x09062004
    CPlugTreeVisualMip002 = 0x09015002
    CPlugVisual001 = 0x09006001
    CPlugVisual004 = 0x09006004
    CPlugVisual005 = 0x09006005
    CPlugVisual009 = 0x09006009
    CPlugVisual00B = 0x0900600B
    CPlugVisual00E = 0x0900600E
    CPlugVisualIndexed001 = 0x0906A001
    CPlugVisual3D002= 0x0902C002
    CPlugVisual3D004= 0x0902C004
    CSceneVehicleCar000 = 0xA02B000
    CSceneMobil003 = 0x0A011003
    CSceneMobil005 = 0x0A011005
    CSceneMobil006 = 0x0A011006
    CSceneObject001 = 0x0A005001
    CSceneObject003 = 0x0A005003
    CSceneObjectLink001 = 0x0A014001
    CSceneObjectLink002 = 0x0A014002
    CSceneObjectLink003 = 0x0A014003
    CScenePoc000 = 0x0A009000
    CSystemConfig008 = 184569864
    CSystemConfig009 = 184569865
    CSystemConfig00B = 184569867
    CSystemConfig020 = 184569888
    CSystemConfig02B = 184569899
    CSystemConfig030 = 184569904
    CSystemConfig034 = 184569908
    CSystemConfig039 = 184569913
    CSystemConfig03A = 184569914
    CSystemConfig03E = 184569918
    CSystemConfig041 = 184569921
    CSystemConfig044 = 184569924
    CSystemConfig045 = 184569925
    CSystemConfig047 = 184569927
    CSystemConfig048 = 184569928
    CSystemConfig049 = 184569929
    CSystemConfig04A = 184569930
    CSystemConfig04C = 184569932
    CSystemConfig04D = 184569933
    CSystemConfig04E = 184569934
    CSystemConfig04F = 184569935
    CSystemConfigDisplay001 = 184627201
    CSystemConfigDisplay003 = 184627203
    CSystemConfigDisplay004 = 184627204
    CSystemConfigDisplay005 = 184627205
    CSystemConfigDisplay008 = 184627208
    CSystemConfigDisplay009 = 184627209
    CSystemConfigDisplay00A = 184627210
    CSystemConfigDisplay00B = 184627211
    CSystemConfigDisplay00F = 184627215
    CSystemConfigDisplay010 = 184627216
    CSystemConfigDisplay011 = 184627217
    CSystemConfigDisplay013 = 184627219
    CSystemConfigDisplay015 = 184627221
    CSystemConfigDisplay016 = 184627222
    CSystemConfigDisplay017 = 184627223
    CSystemConfigDisplay018 = 184627224
    CSystemConfigDisplay019 = 184627225
    CSystemConfigDisplay01B = 184627227
    CSystemConfigDisplay01C = 184627228
    CSystemConfigDisplay01D = 184627229
    CSystemConfigDisplay01E = 184627230
    CSystemConfigDisplay020 = 184627232
    CSystemConfigDisplay021 = 184627233
    CSystemConfigDisplay022 = 184627234
    CTrackManiaReplayRecord000 = 604495872
    CGameCtnBlockInfo005 = 0x24005005
    CGameCtnBlockInfo009 = 0x24005009
    CGameCtnBlockInfo00C = 0x2400500C
    CGameCtnBlockInfo00D = 0x2400500D
    CGameCtnBlockInfo00E = 0x2400500E
    CGameCtnBlockInfo00F = 0x2400500F
    CGameCtnBlockUnitInfo000 = 0x24006000
    CGameCtnBlockUnitInfo001 = 0x24006001
    CGameCtnBlockUnitInfo002 = 0x24006002
    CGameCtnBlockUnitInfo003 = 0x24006003
    CGameCtnBlockUnitInfo004 = 0x24006004
    CGameCtnBlockUnitInfo005 = 0x24006005
    Facade = 0xFACADE01

    @classmethod
    def intIsChunkId(cls, i: int) -> bool:
        """
        Returns whether the provided int is a known chunkId
        :param i: the integer that is tested
        :return: true if i is a known chunkId
        """
        return (i != 0) and (i in set(item.value for item in ChunkId))

    
chunk_id_map = {
    0x24003000 : 0x03043000,
    0x24003002 : 0x03043002,
    0x24003003 : 0x03043003,
    0x24003004 : 0x03043004,
    0x24003005 : 0x03043005,
    0x24003006 : 0x03043006,
    0x24003007 : 0x03043007,
    0x2400300d : 0x0304300d,
    0x24003011 : 0x03043011,
    0x24003014 : 0x03043014,
    0x24003016 : 0x03043016,
    0x24003017 : 0x03043017,
    0x24003018 : 0x03043018,
    0x24003019 : 0x03043019,
    0x2400301C : 0x0304301C,
    0x2400301F : 0x0304301F,
    0x24003021 : 0x03043021,
    0x24003022 : 0x03043022,
    0x24003024 : 0x03043024,
    0x24003025 : 0x03043025,
    0x24003026 : 0x03043026,
    0x24003028 : 0x03043028,
    0x2405F001 : 0x03081001,
    0x2403c000 : 0x0301B000,
    0x2400C001 : 0x0305B001,
    0x2400C004 : 0x0305B004,
    0x2400C005 : 0x0305B005,
    0x2400C006 : 0x0305B006,
    0x2400C008 : 0x0305B008,
    0x2403A002 : 0x03059002,
    0x2405A003 : 0x03080003,
    0x24061001 : 0x03078001,
    0x24061002 : 0x03078002,
    0x24061003 : 0x03078003,
    0x24067002 : 0x030A2002,
    0x24068001 : 0x030A8001,
    0x24068002 : 0x030A8002,
    0x2406B000 : 0x03082000,
    0x2406D001 : 0x03084001,
    0x2406F001 : 0x030A7001,
    0x2406F002 : 0x030A7002,
    0x24075000 : 0x030A9000,
    0x24076003 : 0x03079003,
    0x24076004 : 0x03079004,
    0x24077002 : 0x0307A002,
    0x2407A000 : 0x030A1000,
    0x24081000 : 0x030A5000,
    0x24083000 : 0x030AB000,
    0x24088000 : 0x030A4000,
    0x24089000 : 0x030A6000,
    0x24091001 : 0x0307D001,
    0x24092000 : 0x0, # FIXME who's that pokemon
}



class NodeId(Enum):
    """
    Enum of the supported node ids (see https://wiki.xaseco.org/wiki/Class_IDs for more info)
    """

    Unassigned = 0
    Body = 1
    External = 2
    Direct = 3
    Empty = 0xFFFFFFFF
    CControlEffectSimi = 0x07010000
    CFuncTreeSubVisualSequence = 0x05031000
    CFuncKeysNatural = 0x05030000
    CGameCampaignPlayerScores = 0x030EA000
    CGameCtnBlockSkin = 0x03059000
    CGameCtnBlockInfoClassic = 0x24022000  # TODO figure out real name
    CGameCtnBlockInfoRoad = 0x24023000
    CGameCtnBlockInfoClip = 0x24024000
    CGameCtnBlockInfoFlat = 0x24020000
    CGameCtnBlockInfoRectAsym = 0x24064000
    CGameCtnBlockInfoFrontier = 0x24021000
    CGameCtnBlockUnitInfo2 = 0x24006000  # TODO figure out real name
    CGameCtnBlockUnitInfo = 0x03036000
    CGameCtnChallenge = 0x03043000
    CGameCtnChallengeParameters = 0x0305B000
    CGameCtnCollectorList = 0x0301B000
    CGameCtnGhost = 0x03092000
    CGameCtnMediaBlockCameraCustom = 0x030A2000
    CGameCtnMediaBlockCameraGame = 0x03084000
    CGameCtnMediaBlockCameraPath = 0x030A1000
    CGameCtnMediaBlockCameraEffectShake = 0x030A4000
    CGameCtnMediaBlockFxBloom = 0x03083000
    CGameCtnMediaBlockFxBlurMotion = 0x03082000
    CGameCtnMediaBlockFxBlurDepth = 0x03081000
    CGameCtnMediaBlockFxColors = 0x03080000
    CGameCtnMediaBlockGhost = 0x030E5000
    CGameCtnMediaBlockImage = 0x030A5000
    CGameCtnMediaBlockMusicEffect = 0x30A6000
    CGameCtnMediaBlockSound = 0x030A7000
    CGameCtnMediaBlockText = 0x030A8000
    CGameCtnMediaBlockTime = 0x03085000
    CGameCtnMediaBlockTrails = 0x030A9000
    CGameCtnMediaBlockTransitionFade = 0x030AB000
    CGameCtnMediaBlockTriangles2D = 0x0304B000
    CGameCtnMediaBlockTriangles3D = 0x0304C000
    CGameCtnMediaClip = 0x03079000
    CGameCtnMediaClipGroup = 0x0307A000
    CGameCtnMediaTrack = 0x03078000
    CGameHighScore = 0x3047000
    CGamePlayerOfficialScores = 0x03095000
    CGamePlayerScore = 0x0308D000
    CGameCtnReplayRecord = 0x03093000
    CMwRefBuffer = 0x01026000
    CMotionShader = 0x0802B000
    CMotionPlayer = 0x08034000
    CPlugFileFidCache = 0x09049000
    CPlugShaderApply = 0x09026000
    CPlugSolid = 0x09005000
    CPlugSurface = 0x0900C000
    CPlugSurfaceGeom = 0x0900F000
    CPlugTree = 0x0904F000
    CPlugTreeLight = 0x09062000
    CPlugTreeVisualMip = 0x09015000
    CPlugVisualIndexedTriangles = 0x0901E000
    CPlugMaterial = 0x09079000
    CPlugMaterialCustom = 0x0903A000
    CSceneMobil = 0x0A011000
    CSceneObjectLink = 0x0A014000
    CSceneSoundSource = 0x0A00E000
    CSystemConfig = 0xB0005000
    CTrackManiaReplayRecord = 0x2407E000
    # Skip = int.from_bytes(b"SKIP", "big")

    @classmethod
    def intIsNodeId(cls, i: int) -> bool:
        """
        Returns whether the provided int is a known nodeId
        :param i: the integer that is tested
        :return: true if i is a known nodeId
        """
        return i in set(item.value for item in NodeId)
    
node_id_map = {
    0x24003000 : 0x03043000,
    0x2403c000 : 0x0301B000,
    0x2400C000 : 0x0305B000,
    0x2403A000 : 0x03059000,
    0x2405A000 : 0x03080000,
    0x2405F000 : 0x03081000,
    0x24061000 : 0x03078000,
    0x24067000 : 0x030A2000,
    0x2406F000 : 0x030A7000,
    0x24068000 : 0x030A8000,
    0x2406B000 : 0x03082000,
    0x2406D000 : 0x03084000,
    0x24075000 : 0x030A9000,
    0x24076000 : 0x03079000,
    0x24077000 : 0x0307A000,
    0x2407A000 : 0x030A1000,
    0x24081000 : 0x030A5000,
    0x24083000 : 0x030AB000,
    0x24088000 : 0x030A4000,
    0x24089000 : 0x030A6000,
    0x24092000 : 0x0, # FIXME who's that pokemon
}

