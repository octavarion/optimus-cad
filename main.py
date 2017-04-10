import numpy as np
from geometry import CoordinatesSystem, Point, Vector
from constraints import PointConstraint

rootcs = CoordinatesSystem((1, 1, 0), rotation=(0, 0, 0))

p1 = Point((0, 0, 0), origin=rootcs)
v = Vector(length=1, elevation=np.radians(45), azimuth=np.radians(0), origin=rootcs)
print(v.length)
print(v.endpoint)
p2 = Point((0, 0, 0), origin=v.endpoint)
pc = PointConstraint(p1, p2)
print(pc)
print(p2.origin.origin)
