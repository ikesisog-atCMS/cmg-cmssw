#ifndef GEOMETRY_CALOTOPOLOGY_ECALENDCAPTOPOLOGY_H
#define GEOMETRY_CALOTOPOLOGY_ECALENDCAPTOPOLOGY_H 1

#include "DataFormats/EcalDetId/interface/EEDetId.h"
#include "Geometry/CaloTopology/interface/CaloSubdetectorTopology.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include <vector>
#include <iostream>

class EcalEndcapTopology : public CaloSubdetectorTopology {

 public:
  /// create a new Topology
  EcalEndcapTopology() : theGeom_(0) {};

  /// virtual destructor
  virtual ~EcalEndcapTopology() { }  
  
  /// create a new Topology from geometry
  EcalEndcapTopology(edm::ESHandle<CaloGeometry> theGeom) : theGeom_(theGeom)
    {
    }

  /// move the Topology north (increment iy)
  virtual std::vector<DetId> north(const DetId& id) const
    { 
      EEDetId nextId=incrementIy(EEDetId(id));
      std::vector<DetId> vNeighborsDetId;
      if (! (nextId==EEDetId(0)))
	vNeighborsDetId.push_back(DetId(nextId.rawId()));
      return vNeighborsDetId;
    }

  /// move the Topology south (decrement iy)
  virtual std::vector<DetId> south(const DetId& id) const
    { 
      EEDetId nextId=decrementIy(EEDetId(id));
      std::vector<DetId> vNeighborsDetId;
      if (! (nextId==EEDetId(0)))
	vNeighborsDetId.push_back(DetId(nextId.rawId()));
      return vNeighborsDetId;
    }

  /// move the Topology east (positive ix)
  virtual std::vector<DetId> east(const DetId& id) const
    { 
      EEDetId nextId=incrementIx(EEDetId(id));
      std::vector<DetId> vNeighborsDetId;
      if (! (nextId==EEDetId(0)))
	vNeighborsDetId.push_back(DetId(nextId.rawId()));
      return vNeighborsDetId;
    }

  /// move the Topology west (negative ix)
  virtual std::vector<DetId> west(const DetId& id) const
    { 
      EEDetId nextId=decrementIx(EEDetId(id));
      std::vector<DetId> vNeighborsDetId;
      if (! (nextId==EEDetId(0)))
	vNeighborsDetId.push_back(DetId(nextId.rawId()));
      return vNeighborsDetId;
    }
  
  virtual std::vector<DetId> up(const DetId& /*id*/) const
    {
      std::cout << "EcalBarrelTopology::up() not yet implemented" << std::endl; 
      std::vector<DetId> vNeighborsDetId;
      return  vNeighborsDetId;
    }
  
  virtual std::vector<DetId> down(const DetId& /*id*/) const
    {
      std::cout << "EcalBarrelTopology::down() not yet implemented" << std::endl; 
      std::vector<DetId> vNeighborsDetId;
      return  vNeighborsDetId;
    }

 private:

  /// move the nagivator to larger ix
  EEDetId incrementIx(const EEDetId& id) const ;

  /// move the nagivator to smaller ix
  EEDetId decrementIx(const EEDetId& id) const ;

  /// move the nagivator to larger iy
  EEDetId incrementIy(const EEDetId& id) const ;

  /// move the nagivator to smaller iy
  EEDetId decrementIy(const EEDetId& id) const;

  edm::ESHandle<CaloGeometry> theGeom_;
};

#endif
