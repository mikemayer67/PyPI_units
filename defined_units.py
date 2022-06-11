"""Currently Defined Units"""
import units
from units.leaf_unit import LeafUnit
from units.predefined import define_units

class DefinedUnits(object):
    def __init__(self, load=True):
        if load:
            define_units()
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
