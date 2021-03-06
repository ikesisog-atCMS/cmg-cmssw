# Configuration file to run stubs/CSCGeometryAnalyser
# to dump CSC geometry information
# Tim Cox 20.01.2009

import FWCore.ParameterSet.Config as cms

process = cms.Process("GeometryTest")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("Geometry.MuonCommonData.muonEndcapIdealGeometryXML_cfi")
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
##process.load("Geometry.CSCGeometryBuilder.idealForDigiCscGeometry_cff")
process.load("Alignment.CommonAlignmentProducer.FakeAlignmentSource_cfi")
##process.preferFakeAlign = cms.ESPrefer("FakeAlignmentSource", "FakeAlignmentSource")
process.fake2 = process.FakeAlignmentSource
del process.FakeAlignmentSource
process.preferFakeAlign = cms.ESPrefer("FakeAlignmentSource", "fake2")

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(1)
)

process.MessageLogger = cms.Service(
   'MessageLogger',
   destinations = cms.untracked.vstring('cout'),
   categories = cms.untracked.vstring(
     'CSC',
     'CSCNumbering',
     'CSCGeometryBuilderFromDDD',
     'RadialStripTopology'
   ),
   debugModules = cms.untracked.vstring('*'),
   cout = cms.untracked.PSet(
      noLineBreaks = cms.untracked.bool(True),
      threshold = cms.untracked.string('DEBUG'),
      default = cms.untracked.PSet(
         limit = cms.untracked.int32(0) # none
      ),
      CSC = cms.untracked.PSet(
         limit = cms.untracked.int32(-1) # all
      ),
      CSCNumbering = cms.untracked.PSet(
         limit = cms.untracked.int32(0) # none - attempt to match tcg_db.py output
      ),
      CSCGeometryBuilderFromDDD = cms.untracked.PSet(
         limit = cms.untracked.int32(-1) # all
      ),
      RadialStripTopology = cms.untracked.PSet(
         limit = cms.untracked.int32(-1) # all
      )
   )
)

process.producer = cms.EDAnalyzer("CSCGeometryAnalyzer")

process.p1 = cms.Path(process.producer)
process.CSCGeometryESModule.debugV = True

