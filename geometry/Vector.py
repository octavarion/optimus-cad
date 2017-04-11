from . import CoordinatesSystem, Geometry, init_geometry
import numpy as np
import math


class Vector(Geometry):
    @init_geometry
    def __init__(self, coordinates=None, length=0, elevation=0, azimuth=0):
        self._origin = None
        self.coordinates = coordinates

        if self.coordinates is None:
            self.coordinates = (0, 0, 0)
            self.length = length
            self.elevation = elevation
            self.azimuth = azimuth

    @property
    def origin(self) -> CoordinatesSystem:
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value

    @property
    def length(self):
        return np.linalg.norm(self.coordinates)

    @length.setter
    def length(self, value):
        xy = value * math.cos(self.elevation)
        z = value * math.sin(self.elevation)
        y = xy * math.cos(self.azimuth)
        x = xy * math.sin(self.azimuth)
        self.coordinates = (x, y, z)

    @property
    def elevation(self):
        x, y, z = self.coordinates
        return math.atan2(z, math.sqrt(x**2 + y**2))

    @elevation.setter
    def elevation(self, value):
        z = self.length * math.sin(value)
        xy = self.length * math.cos(value)
        y = xy * math.cos(self.azimuth)
        x = xy * math.sin(self.azimuth)
        self.coordinates = (x, y, z)

    @property
    def azimuth(self):
        x, y, z = self.coordinates
        return math.atan2(y, x)

    @azimuth.setter
    def azimuth(self, value):
        z = self.length * math.sin(self.elevation)
        xy = self.length * math.cos(self.elevation)
        y = xy * math.cos(value)
        x = xy * math.sin(value)
        self.coordinates = (x, y, z)

    @property
    def endpoint(self) -> CoordinatesSystem:
        # translation = tuple(np.add(self.origin.origin, self.coordinates))
        rotation = (self.elevation, 0, self.azimuth)
        return CoordinatesSystem(origin=self.coordinates, rotation=rotation, parent=self.origin)

    @endpoint.setter
    def endpoint(self, value: CoordinatesSystem):
        # coordinates = tuple(np.subtract(value.origin, self.origin.origin))
        self.coordinates = value.origin

    def render(self):
        return None
