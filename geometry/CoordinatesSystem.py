import numpy as np
from transforms3d.euler import euler2mat


class CoordinatesSystem(object):
    def __init__(self, origin, rotation=(0, 0, 0), parent=None):
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
            parent_absolute = self.parent.absolute
            parent_vector = parent_absolute.origin
            print(f'parent vector: {parent_vector}')
            print(f'rotation: {parent_absolute.rotation}')
            print(origin)
            self_vector = np.dot(origin, euler2mat(*parent_absolute.rotation))
            print(f'self_vector: {self_vector}')
            absolute_vector = np.add(self_vector, parent_vector)
            return CoordinatesSystem(origin=absolute_vector, parent=parent_absolute.parent)
        else:
            return self

    def __str__(self):
        return f'x: {self.x}, y: {self.y}, z: {self.z} | roll: {self.rotation[0]}, pitch: {self.rotation[1]}, yaw: {self.rotation[2]}'
