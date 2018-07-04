RootFile = "/data/lhcb04/mschiller/SummerProject2018/Bu2JpsiKplus_MC_Down_Upgrade_OptSummer2017.root"
TupleName = "Bu2JpsiKplusDetached/DecayTree"
CalibrationMode = "Bu"
UseWeight = 0
Nmax = 50000
#BranchWeight = "SigYield_sw"
#selection

#OS_Combintation_Use = 1
#OS_Combintation_BranchDec = "B_TAGDECISION_OS"
#OS_Combintation_BranchProb = "B_TAGOMEGA_OS"

SS_Pion_Use = 1
#SS_Pion_TypeDec = "Short_t"
SS_Pion_BranchDec = "lab0_SSPion_TAGDEC"
#SS_Pion_TypeProb = "Float_t"
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

#OS_Electron_Use = 1
#OS_Electron_BranchDec = "lab0_OSElectronLatest_TAGDEC"
#OS_Electron_BranchProb = "lab0_OSElectronLatest_TAGETA"
#OS_Electron_Write = 1

OS_Charm_Use = 1
OS_Charm_BranchDec = "lab0_OSCharm_TAGDEC"
OS_Charm_BranchProb = "lab0_OSCharm_TAGETA"
OS_Charm_Write = 1

SS_Proton_Use = 1
SS_Proton_BranchDec = "lab0_SSProton_TAGDEC"
SS_Proton_BranchProb = "lab0_SSProton_TAGETA"
SS_Proton_Write = 1


DoCalibrations = 1
BranchID = "lab0_TRUEID"
UseNewtonRaphson = 0

PerformOfflineCombination_OSplusSS = 1
OS_Combination_InComb = 1
SS_Pion_InComb = 1
OS_Charm_InComb = 1
SS_Proton_InComb = 1
VtxCharge_InComb = 1
OS_Muon_InComb = 1
OS_Kaon_InComb = 1

