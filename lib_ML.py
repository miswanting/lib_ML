# coding=utf-8
import math
import numpy as np
import random


class PointSurface(object):
    """docstring for PointSurface."""
    random_static_rate = 1
    ramdom_dynamic_rate = 1

    def __init__(self, dimension=2, debug=False):
        super(PointSurface, self).__init__()
        self.debug = debug
        self.dimension = dimension
        self.list_points = []

    def set_point(self, point):
        tmp = list(point)
        if len(tmp) == self.dimension:
            for i, each in enumerate(self.list_points):
                if each[:-1] == tmp[:-1]:
                    del self.list_points[i]
            self.list_points.append(tmp)

    def get_point_value(self, point):
        tmp = list(point)
        nearest_point = []
        nearest_distance = 'N/A'
        if len(tmp) == self.dimension - 1:
            for each in self.list_points:
                distance = 0
                for i in range(0, self.dimension - 1):
                    distance += (each[i] - tmp[i]) ** 2
                distance = math.sqrt(distance)
                if nearest_distance == 'N/A':
                    nearest_distance = distance
                    nearest_point = each
                elif nearest_distance > distance:
                    nearest_distance = distance
                    nearest_point = each
            values = []
            for each in nearest_point[-1]:
                value = random.uniform(-1, 1)
                value *= (self.random_static_rate +
                          self.ramdom_dynamic_rate * nearest_distance)
                value += each
                values.append(value)
        return values


if __name__ == '__main__':
    I = PointSurface(debug=True)
    I.set_point((1, [1]))
    I.set_point((2, [2]))
    I.set_point((3, [3]))
    for i in range(0, 300):
        print(I.get_point_value([i / 100])[0])
