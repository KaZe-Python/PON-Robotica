# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time as t

def eratostene(lim):
    m=lim+1
    a = [True] * m
    a[0] = a[1] = False

    for i in range(2, int(lim**0.5+1)):
        if a[i]:
            for j in range(i*i, lim+1, i):
                a[j] = False
    return [x for x in range(2,lim+1) if a[x]]

def prime_f(n, factors):
    for fact in factors:
        if n % fact != 0:
            fact.remove(n)
    return fact

# Tempo impiegato per calcolare un prodotto

s = t.time()
x, y = 6700417, 2147483647
z = x*y
e = t.time()
dt = e-s
print("Tempo: " , dt)

# Tempo per fattorizzare un numero

s = t.time()
print("Inizio Crivello")
# Tempo per crivello
factors = eratostene(int(1e9))
e = t.time()
print("Fine! Tempo crivello: ", e-s)

s = t.time()
print("Inizio Fattorizzazione")
fp_1 = prime_f(z, factors)
e = t.time()
dt = e-s
print("Fine! Tempo fattorizzazione: ", dt)