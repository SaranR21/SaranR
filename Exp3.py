#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:53:41 2019

@author: saran
"""

import numpy as np
from matplotlib import pyplot as plt

def dft(x):
    N=len(x)
    X=[]
    for i in range(N):
        temp=0
        for j in range(N):
            temp+=x[j]*np.exp((0-1j)*2*np.pi*i*j/N)
        X.append(temp)
    return np.array(X)

f1=2
f2=5

#Linearity
a=5
b=3

t=np.linspace(0,1,50)
#signal
x1=np.sin(2*np.pi*f1*t)
x2=np.sin(2*np.pi*f2*t)
x=(a*x1)+(b*x2)


fs=4*max(f1,f2)
n=np.arange(0,64)
x1_n=np.sin(2*np.pi*n*f1/fs)
x2_n=np.sin(2*np.pi*n*f2/fs)

x_n=(a*x1_n)+(b*x2_n)

X1=dft(x1_n)
X2=dft(x2_n)
X=dft(x_n)
X_0=(a*X1)+(b*X2)

fig,axes = plt.subplots(nrows=3, ncols=2)
axes[0,0].plot(t,x)
axes[0,1].stem(n,x_n)
axes[1,0].stem(X1)
axes[1,1].stem(X2)
axes[2,0].stem(X)
axes[2,1].stem(X_0)

#Time shift
x_n1=np.zeros(len(x_n))
for i in range(len(x_n)):
    x_n1[i]=x_n[i-3]

X_1=dft(x_n1)
X_2=np.zeros(len(X))
for i in range(len(X)):
    X_2[i]+=X[i]*np.exp((0-1j)*2*np.pi*3*i/len(X))
        
fig2,axes = plt.subplots(nrows=2, ncols=2)
axes[0,0].stem(n,x_n)
axes[0,1].stem(n,x_n1)
axes[1,0].stem(X_1)
axes[1,1].stem(X_2)

#frequency shift

X_3 = np.zeros(len(X))
for i in range(len(X)):
    X_3[i]=X[i-3]

x_n4=np.zeros(len(x_n))
for i in range(len(x_n)):
    x_n4[i]=x_n[i]*np.exp((0+1j)*2*np.pi*3*i)

X_4 = dft(x_n4)
fig3, axes = plt.subplots(nrows=1, ncols=2)
axes[0].stem(X_3)
axes[1].stem(X_4)
          

        



