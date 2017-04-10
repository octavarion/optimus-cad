import numpy as np
from geometry import CoordinatesSystem, Point, Vector
from constraints import PointConstraint

root = CoordinatesSystem((0, 0, 0), rotation=(np.radians(90), 0, 0))
root2 = CoordinatesSystem((1, 1, 0), parent=root)
root3 = CoordinatesSystem((1, 0, 0), parent=root2)

p1 = Point(origin=root2)
v = Vector(length=1, elevation=np.radians(0), azimuth=np.radians(0), origin=root2)
p2 = Point(origin=v.endpoint)

print(p2.origin)
print(p2.origin.absolute)
print(v.coordinates)
