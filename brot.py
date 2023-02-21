# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:27:42 2022

@author: A Ramsey
"""

import numpy as np
import matplotlib.pyplot as plt
'''
set of complex numbers c for which 
the function f(z) = z^2 + c does not
diverge to infinity when iterated from
z = 0 
'''

def F(z, c):
    return (z**2) + c

def brot_centre(c):
    z1 = 0
    z2 = F(z1, c)
    count = 0
    while abs(z1 - z2) < 1e35:
        z1 = z2
        z2 = F(z1, c)
        count += 1
        if count > 300:
            return count
    return count

#brot
a = np.linspace(-2, 1, 500)
b = np.linspace(-1, 1, 500)

#seahorse valley
c = np.linspace(-1, -0.5, 500)
d = np.linspace(0, 0.5, 500)
e = np.linspace(-0.75, -0.7, 500)
f = np.linspace(0.15, 0.2, 500)
g = np.linspace(-0.75, -0.73, 500)
h = np.linspace(0.16, 0.18, 500)
i = np.linspace(-0.742, -0.736, 1000)
j = np.linspace(0.172, 0.178, 1000)
k = np.linspace(-0.7395, -0.739, 500)
l = np.linspace(0.1745, 0.1755, 500)
m = np.linspace(-0.73925, -0.73915, 500)
n = np.linspace(0.1749, 0.175, 500)

#mini brot
o = np.linspace(-2, -1.5, 500)
p = np.linspace(-0.125, 0.125, 500)

#tendrils
q = np.linspace(-1.25, -1, 500)
r = np.linspace(0.125, 0.375, 500)
s = np.linspace(-1.175, -1.15, 500)
t = np.linspace(0.275, 0.3, 500)
u = np.linspace(-1.165, -1.16, 500)
v = np.linspace(0.29, 0.295, 500)

#opposite seahorse valley
w = np.linspace(-0.9, -0.85, 500)
x = np.linspace(0.2, 0.3, 500)
y = np.linspace(-0.865, -0.86, 500)
z = np.linspace(0.27, 0.28, 500)

#elephant valley
aa = np.linspace(0.125, 0.375, 500)
ab = np.linspace(-0.125, 0.125, 500)
ac = np.linspace(0.3, 0.375, 500)
ad = np.linspace(-0.05, -0.0125, 500)
ae = np.linspace(0.315, 0.335, 500)
af = np.linspace(-0.0425, -0.0325, 500)
ag = np.linspace(0.32825, 0.33125, 500)
ah = np.linspace(-0.0425, -0.038, 500)
ai = np.linspace(0.32925, 0.33, 500)
aj = np.linspace(-0.04, -0.0395, 500)

#scepter valley
ak = np.linspace(-1.28, -1.22, 500)
aj = np.linspace(-0.05, 0.05, 500)
al = np.linspace(-1.266, -1.261, 500)
am = np.linspace(0.04, 0.048, 500)
an = np.linspace(-1.2652, -1.2638, 500)
ao = np.linspace(0.043, 0.0455, 500)
ap = np.linspace(-1.264825, -1.26465, 500)
aq = np.linspace(0.04318, 0.04332, 500)

def makes_matrix(a, b):
    tot_matrix = []
    b_array = []
    
    for x in a:
        for y in b:
            c = x + y*1j
            div_or_conv = brot_centre(c)
            b_array.append(div_or_conv)
            
        tot_matrix.append(b_array)
        b_array = []
        
    tot_matrix = np.array(tot_matrix)
    tot_matrix = np.ndarray.transpose(tot_matrix)
    
    return tot_matrix

fig, ax = plt.subplots()
plot = ax.pcolormesh(i, j, makes_matrix(i, j))
plt.colorbar(plot)
plt.show()