from abc import ABC, abstractmethod
from . import CoordinatesSystem


# class GeometryMeta(type):
#     attributes = ['origin', 'visible']
#
#     def __new__(cls, clsname, superclasses, attributedict):
#         old_init = attributedict['__init__'] if '__init__' in attributedict else None
#
#         def new_init(self, *args, **kwargs):
#             origin = None
#             if 'origin' in kwargs:
#                 origin = kwargs['origin']
#                 del kwargs['origin']
#             if old_init is not None:
#                 old_init(self, *args, **kwargs)
#             if origin is not None:
#                 self.origin = origin
#         attributedict['__init__'] = new_init
#         return type.__new__(cls, clsname, superclasses, attributedict)

def init_geometry(func):
    def init_wrapper(self: Geometry, *args, origin=None, visible=True, **kwargs):
        result = func(self, *args, **kwargs)
        self.origin = origin
        self.visible = visible
        return result
    return init_wrapper


class Geometry(ABC):
    origin: CoordinatesSystem = None

    @abstractmethod
    def render(self):
        pass
