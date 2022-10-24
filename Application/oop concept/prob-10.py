"""  
 Write a Python class named Distance constructed by two points (x1, y1), (x2, y2) and a method which will compute the distance between those points.
"""

import math

class Distance:
    def __init__(self, x1, y1,x2,y2):
        self.p1 = (x1,y1)
        self.p2 = (x2,y2)
    def compute_dis(self):
        distance = math.sqrt( ((self.p1[0]-self.p2[0])**2)+((self.p1[1]-self.p2[1])**2) )
        return distance


point = Distance(4,9,10,5)
print(point.compute_dis())