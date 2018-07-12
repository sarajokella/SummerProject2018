RootFile = "@@6@@"
TupleName = "@@7@@" 
Nmax = @@1@@
Selection = "@@2@@"

@@3@@SaveCalibrationsToXML = 1
CalibrationMode = "Bu"
DoCalibrations = 1

BranchID = "lab0_TRUEID"
UseWeight = 0
UseNewtonRaphson = 0

######Branch Info###############

SS_Pion_Use = 1
SS_Pion_BranchDec = "lab0_SSPion_TAGDEC"
SS_Pion_BranchProb = "lab0_SSPion_TAGETA"
SS_Pion_Use = 1
SS_Pion_Write = 1

OS_Kaon_Use = 1
OS_Kaon_BranchDec = "lab0_OSKaonLatest_TAGDEC"
OS_Kaon_BranchProb = "lab0_OSKaonLatest_TAGETA"
OS_Kaon_Write = 1

VtxCharge_Use = 1
VtxCharge_BranchDec = "lab0_OSVtxCh_TAGDEC"
VtxCharge_BranchProb = "lab0_OSVtxCh_TAGETA"
VtxCharge_Write = 1

OS_Muon_Use = 1
OS_Muon_BranchDec = "lab0_OSMuonLatest_TAGDEC"
OS_Muon_BranchProb = "lab0_OSMuonLatest_TAGETA"
OS_Muon_Write = 1

OS_Charm_Use = 1
OS_Charm_BranchDec = "lab0_OSCharm_TAGDEC"
OS_Charm_BranchProb = "lab0_OSCharm_TAGETA"
OS_Charm_Write = 1

SS_Proton_Use = 1
SS_Proton_BranchDec = "lab0_SSProton_TAGDEC"
SS_Proton_BranchProb = "lab0_SSProton_TAGETA"
SS_Proton_Write = 1

####Combination##############

PerformOfflineCombination_OS = 1
OS_Kaon_InOSComb = 1
OS_Muon_InComb = 1
OS_Charm_InOSComb = 1
VtxCharge_InOSComb = 1

@@4@@PerformOfflineCombination_OSplusSS = 1
@@4@@OS_Combination_InComb = 1
@@4@@SS_Pion_InComb = 1
##SS_Proton_InComb = 1

@@4@@OS_Combination_CalibrationArchive = "../@@5@@/OS_Combination_Calibration.xml"
@@4@@SS_Pion_CalibrationArchive = "../@@5@@/SS_Pion_Calibration.xml"
