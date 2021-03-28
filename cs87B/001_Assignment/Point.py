#!/usr/bin/env python3

from math import *

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distnace_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def distnace(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Point3D(Point):
    z = 0
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z
    
    def translate(self, dx, dy, dz):
        Point.translate(self, dx, dy)
        self.z += dz
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

def main():
    p = Point()
    p3 = Point3D()
    print(p)
    print(p3)

if __name__ == "__main__":
    main()