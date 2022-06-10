"""Currently Defined Units"""
import units
from units.leaf_unit import LeafUnit

class DefinedUnits(object):
    def __init__(self):
        for k,v in units.REGISTRY.items():
            setattr(self,k,v)

    def __getattr__(self,k):
        if k in units.REGISTRY:
            return units.REGISTRY[k]
        unit = units.unit(k)
        if type(unit) is LeafUnit:
            del units.REGISTRY[k]
            return None
        return unit
