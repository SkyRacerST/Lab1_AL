#!/usr/bin/env python3
# -*- coding: utf-8 -*-

pi = 3.1415926

def circle_area(radius):
	return round(pi * radius ** 2, 4)

def point_inside(point, radius):
	dist = (point[0] ** 2 + point[1] ** 2) ** 0.5
	return dist < radius

def main():
    radius = 42
    print(circle_area(radius))
    print(point_inside((23, 34), radius))
    print(point_inside((30, 30), radius))

if __name__ == '__main__':
    main()