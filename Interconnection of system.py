# -*- coding: utf-8 -*-
"""
Created on Wed Aug 07 11:43:08 2019

@author: CB.EN.U4ECE18248
"""

import numpy as np
from matplotlib import pyplot as plt

def convolution(x,h_0):
    y = np.zeros(len(x)+len(h_0)-1)
    for i in range(len(x)+len(h_0)-1):
        for j in range(i+1):
            if j < len(x) and i- j < len(h_0):
                y[i] += x[j]*h_0[i-j]
    return y
    
def shift(x,a):
    for i in range(len(x)):
        if i == a:
            x[i] = 1
        else :
            x[i] = 0
    return x
h = np.zeros(3)
h1_1 = shift(h,2)
h = np.zeros(3)
h1_2 = shift(h,0)
h1 = h1_1+h1_2
n = np.arange(13)     
h2 = np.sin(2*np.pi*n/13)  
n1 = np.arange(15)
h3 = np.sin(2*np.pi*n1/15)
h = np.zeros(4)
h4_1 = shift(h,1)
h = np.zeros(4)
h4_2 = shift(h,3)
h4 = h4_1+h4_2


h12 = convolution(h1,h2)
h123 = h12 + h3
h1234 = convolution(h123,h4)

plt.title("Interconnection of Systems")
plt.subplot(711)
plt.xlabel('n')
plt.ylabel('h1')
plt.stem(np.arange(len(h1)),h1)
plt.subplot(712)
plt.xlabel('n')
plt.ylabel('h2')
plt.stem(np.arange(len(h2)),h2)
plt.subplot(713)
plt.xlabel('n')
plt.ylabel('h3')
plt.stem(np.arange(len(h3)),h3)
plt.subplot(714)
plt.xlabel('n')
plt.ylabel('h4')
plt.stem(np.arange(len(h4)),h4)
plt.subplot(715)
plt.xlabel('n')
plt.ylabel('h12')
plt.stem(np.arange(len(h12)),h12)
plt.subplot(716)
plt.xlabel('n')
plt.ylabel('h123')
plt.stem(np.arange(len(h123)),h123)
plt.subplot(717)
plt.xlabel('n')
plt.ylabel('h1234')
plt.stem(np.arange(len(h1234)),h1234)

