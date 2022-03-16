# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:30:00 2022

@author: bpcos
"""
import numpy as np
import math
#import random as rd


x = np.array([1.8, 3.0, 9.9, 9.5])
y = np.array([0.2, 9.9, 5.3, 1.6])
pts = [(1.8, 0.2), (3.0, 9.9), (9.9, 5.3), (9.5, 1.6)]

diff = lambda p: (p[0][0]-p[1][0], p[0][1]-p[1][1])
diffs = map(diff, zip(pts[:-1], pts[1:]))
path = sum(math.hypot(d1,d2) for d1, d2 in diffs)

print (path)