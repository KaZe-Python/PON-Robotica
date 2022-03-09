# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:21:48 2022

@author: bpcos
"""

import time as t
import random as rnd
from matplotlib import pyplot as plt

def bb_sort(x):
  dim = len(x)
  stop=0
  
  while(stop < dim - 1):
    for i in range(0, dim-1):
      if x[i] > x[i+1]:
        x[i+1], x[i] = x[i], x[i+1]
        continue
      stop += 1
p = 1000
dim = [x*p for x in range(1,91)]
ts = []

for i in dim:
  vals = rnd.sample(range(0, i), i)
  s = t.time()
  bb_sort(vals)
  e = t.time()
  ts.append((e-s))

for i in range(0,len(ts)-1):
  print(f"Lista di {(i+1)*p} numeri, Tempo #{i}: {ts[i]}")

plt.plot(dim, ts, 'o', ms=5, color='Red')