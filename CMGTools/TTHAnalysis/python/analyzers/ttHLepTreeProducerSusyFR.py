from CMGTools.TTHAnalysis.analyzers.ttHLepTreeProducerNew import *

class ttHLepTreeProducerSusyFR( ttHLepTreeProducerNew ):

    #-----------------------------------
    # TREE PRODUCER FOR THE TTH ANALYSIS
    #-----------------------------------
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(ttHLepTreeProducerSusyFR,self).__init__(cfg_ana, cfg_comp, looperName)

        ## Declare what we want to fill
        self.globalVariables = [ 
            NTupleVariable("nLepGood20",  lambda ev: sum([(l.pt() > 20)                   for l in ev.selectedLeptons]), int, help="Number of leptons with pt > 20 (loose id)"),
            NTupleVariable("nLepGood10",  lambda ev: sum([(l.pt() > 10)                   for l in ev.selectedLeptons]), int, help="Number of leptons with pt > 10 (loose id)"),
            NTupleVariable("nLepTight20", lambda ev: sum([(l.pt() > 20 and l.tightFakeId) for l in ev.selectedLeptons]), int, help="Number of leptons with pt > 20 (tight id)"),
            NTupleVariable("nLepTight10", lambda ev: sum([(l.pt() > 10 and l.tightFakeId) for l in ev.selectedLeptons]), int, help="Number of leptons with pt > 10 (tight id)"),
            NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"),
            NTupleVariable("nJet30", lambda ev: len(ev.cleanJets), int, help="Number of jets with pt > 25"),
            NTupleVariable("nBJetMedium30", lambda ev: len(ev.bjetsMedium), int, help="Number of jets with pt > 25 passing CSV medium"),
            NTupleVariable("nJet40", lambda ev: sum([j.pt() > 40 for j in ev.cleanJets]), int, help="Number of jets with pt > 40"),
            NTupleVariable("nBJetMedium40", lambda ev: sum([j.btagWP("CSVM") for j in ev.bjetsMedium if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV medium"),
            NTupleVariable("htJet30", lambda ev : ev.htJet25, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 30 GeV)"),
            NTupleVariable("mhtJet30", lambda ev : ev.mhtJet25, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 30 GeV)"),
            NTupleVariable("htJet40j", lambda ev : ev.htJet40j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("htJet40", lambda ev : ev.htJet40, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("mhtJet40", lambda ev : ev.mhtJet40, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("mZ1", lambda ev : ev.bestZ1[0], help="Best m(ll) SF/OS"),
            NTupleVariable("mZ2", lambda ev : ev.bestZ2[3], help="m(ll) of second SF/OS pair, for ZZ reco."),
            NTupleVariable("mZ1SFSS", lambda ev : ev.bestZ1sfss[0], help="Best m(ll) SF/SS"),
            NTupleVariable("minMllSFOS", lambda ev: ev.minMllSFOS, help="min m(ll), SF/OS"),
            NTupleVariable("maxMllSFOS", lambda ev: ev.maxMllSFOS, help="max m(ll), SF/OS"),
            NTupleVariable("minMllAFOS", lambda ev: ev.minMllAFOS, help="min m(ll), AF/OS"),
            NTupleVariable("maxMllAFOS", lambda ev: ev.maxMllAFOS, help="max m(ll), AF/OS"),
            NTupleVariable("minMllAFSS", lambda ev: ev.minMllAFSS, help="min m(ll), AF/SS"),
            NTupleVariable("maxMllAFSS", lambda ev: ev.maxMllAFSS, help="max m(ll), AF/SS"),
            NTupleVariable("minMllAFAS", lambda ev: ev.minMllAFAS, help="min m(ll), AF/AS"),
            NTupleVariable("maxMllAFAS", lambda ev: ev.maxMllAFAS, help="max m(ll), AF/AS"),
            NTupleVariable("m2l", lambda ev: ev.m2l, help="m(ll)"),
            NTupleVariable("m3l", lambda ev: ev.m3l, help="m(3l)"),
            NTupleVariable("m4l", lambda ev: ev.m4l, help="m(4l)"),
            NTupleVariable("pt2l", lambda ev: ev.pt2l, help="p_{T}(ll)"),
            NTupleVariable("pt3l", lambda ev: ev.pt3l, help="p_{T}(3l)"),
            NTupleVariable("pt4l", lambda ev: ev.pt4l, help="p_{T}(4l)"),
            NTupleVariable("ht3l", lambda ev: ev.ht3l, help="H_{T}(3l)"),
            NTupleVariable("ht4l", lambda ev: ev.ht4l, help="H_{T}(4l)"),
            NTupleVariable("q3l", lambda ev: ev.q3l, int, help="q(3l)"),
            NTupleVariable("q4l", lambda ev: ev.q4l, int, help="q(4l)"),
            ##--------------------------------------------------
            NTupleVariable("minMWjj", lambda ev: ev.minMWjj, int, help="minMWjj"),
            NTupleVariable("minMWjjPt", lambda ev: ev.minMWjjPt, int, help="minMWjjPt"),
            NTupleVariable("bestMWjj", lambda ev: ev.bestMWjj, int, help="bestMWjj"),
            NTupleVariable("bestMWjjPt", lambda ev: ev.bestMWjjPt, int, help="bestMWjjPt"),
            NTupleVariable("bestMTopHad", lambda ev: ev.bestMTopHad, int, help="bestMTopHad"),
            NTupleVariable("bestMTopHadPt", lambda ev: ev.bestMTopHadPt, int, help="bestMTopHadPt"),
            ##--------------------------------------------------
            NTupleVariable("GenHiggsDecayMode", lambda ev : ev.genHiggsDecayMode, int, mcOnly=True, help="H decay mode (15 = tau, 23/24 = W/Z)"),
            NTupleVariable("GenHeaviestQCDFlavour", lambda ev : ev.heaviestQCDFlavour, int, mcOnly=True, help="pdgId of heaviest parton in the event (after shower)"),
        ]

        self.globalObjects = {
            "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after type 1 corrections"),
            #"metNoPU" : NTupleObject("metNoPU", fourVectorType, help="PF noPU E_{T}^{miss}"),
        }
        self.collections = {
            "selectedLeptons" : NTupleCollection("LepGood", leptonTypeSusyFR, 8, help="Leptons after the preselection"),
            #"selectedTaus"    : NTupleCollection("TauGood", tauTypeTTH, 3, help="Taus after the preselection"),
            "cleanJets"       : NTupleCollection("Jet",     jetTypeTTH, 8, sortDescendingBy = lambda jet : jet.pt(), help="Cental jets after full selection and cleaning, sorted by b-tag"),
            "cleanJetsFwd"    : NTupleCollection("JetFwd",  jetTypeTTH, 4, help="Cental jets after full selection and cleaning, sorted by b-tag"),
            ##--------------------------------------------------
            "gentopquarks"    : NTupleCollection("GenTop",     genParticleType, 2, help="Generated top quarks from hard scattering"),
            "genbquarks"      : NTupleCollection("GenBQuark",  genParticleType, 2, help="Generated bottom quarks from top quark decays"),
            "genwzquarks"     : NTupleCollection("GenQuark",   genParticleWithSourceType, 6, help="Generated quarks from W/Z decays"),
            "genleps"         : NTupleCollection("GenLep",     genParticleWithSourceType, 6, help="Generated leptons from W/Z decays"),
            "gentauleps"      : NTupleCollection("GenLepFromTau", genParticleWithSourceType, 6, help="Generated leptons from decays of taus from W/Z/h decays"),
        }
        if hasattr(self.cfg_ana, 'doInclusiveLeptons') and self.cfg_ana.doInclusiveLeptons:
            self.collections["inclusiveLeptons"] = NTupleCollection("Lep", leptonTypeTTH, 8, help="Leptons without preselection"),
        if hasattr(self.cfg_ana, 'doInclusiveTaus') and self.cfg_ana.doInclusiveTaus:
            self.collections["inclusiveTaus"   ] = NTupleCollection("Tau", tauTypeTTH, 3, help="Taus after the loose preselection"),

        ## Now book the variables
        self.initDone = True
        self.declareVariables()

    def process(self, iEvent, event):
        self.readCollections( iEvent )
        #for i,j in enumerate(event.cleanJets): print "%2d ---> pt = %6.2f, eta = %+5.3f" % (i,j.pt(),j.eta())
        self.fillTree(iEvent, event)
