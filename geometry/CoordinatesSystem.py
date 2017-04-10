import numpy as np


class CoordinatesSystem(object):
    def __init__(self, origin, rotation=None, parent=None):
        self.origin = origin
        self.rotation = rotation
        self.parent: CoordinatesSystem = parent

        self._x, self._y, self._z = origin

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def absolute(self):
        origin = self.origin
        rotation = self.rotation
        if self.parent is not None:
            origin = tuple(np.add(origin, self.parent.absolute.origin))
        return CoordinatesSystem(origin=origin, rotation=rotation, parent=None)

    def __str__(self):
        return f'x: {self.x}, y: {self.y}, z: {self.z} | yaw: {self.rotation[0]}, pitch: {self.rotation[1]}, roll: {self.rotation[2]}'
