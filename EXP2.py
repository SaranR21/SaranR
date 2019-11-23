# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sfp

def dft(x):
    N=len(x)
    X=[]
    for i in range(N):
        temp=0
        for j in range(N):
            temp+=x[j]*np.exp((0-1j)*2*np.pi*i*j/N)
        X.append(temp)
    return X

def mat(x):
    N=len(x)
    X=[]
    for i in range(N):
        for j in range(N):
            X.append(np.exp((0-1j)*2*np.pi*i*j/N))
    return X

f1=2
f2=5
a=5
t1=np.linspace(0,1,500)
#signal
x=a*(np.sin(2*np.pi*f1*t1)+np.sin(2*np.pi*f2*t1))

fs=4*max(f1,f2)
n1=np.arange(0,16)
x_n1=a*(np.sin(2*np.pi*n1*f1/fs)+np.sin(2*np.pi*n1*f2/fs))
n2=np.arange(0,32)
x_n2=a*(np.sin(2*np.pi*n2*f1/fs)+np.sin(2*np.pi*n2*f2/fs))
n3=np.arange(0,64)
x_n3=a*(np.sin(2*np.pi*n3*f1/fs)+np.sin(2*np.pi*n3*f2/fs))


fig,axes=plt.subplots(nrows=4,ncols=2)
axes[0,0].plot(t1,x)
axes[0,1].stem(np.arange(len(sfp.fft(x))),sfp.fft(x))
axes[0,1].set_xlim(0,10)
axes[1,0].stem(np.linspace(0,fs,16),np.angle(dft(x_n1)))
axes[1,1].stem(np.linspace(0,fs,16),dft(x_n1))
axes[2,0].stem(np.linspace(0,fs,32),np.angle(dft(x_n2)))
axes[2,1].stem(np.linspace(0,fs,32),dft(x_n2))
axes[3,0].stem(np.linspace(0,fs,64),np.angle(dft(x_n3)))
axes[3,1].stem(np.linspace(0,fs,64),dft(x_n3))
for i in range(4):
    for j in range(2):
        axes[i,j].set_xlabel('n')
axes[0,0].set_xlabel('t')
axes[0,0].set_ylabel('x(t)')
axes[1,0].set_ylabel('phase(16 bit)')
axes[2,0].set_ylabel('phase(32 bit)')
axes[3,0].set_ylabel('phase(64 bit)')
axes[0,1].set_ylabel('FFT(x)')
for i in range(1,4):
    axes[i,1].set_ylabel('real')
axes[0,0].set_title('CB.EN.U4ECE18248')
plt.savefig('CB.EN.U4ECE18248_3.png')

W=np.matrix(mat(x_n1)).reshape(16,16)
X=x_n1*W
X=X.T
W1=sfp.fft(x_n1)
fig2,axes=plt.subplots(nrows=2,ncols=2)
axes[0,0].stem(np.linspace(0,fs,16),np.real(X))
axes[0,0].set_ylabel('DFT real')
axes[0,0].set_title('CB.EN.U4ECE18248')
axes[1,0].stem(np.linspace(0,fs,16),np.angle(X))
axes[1,0].set_ylabel('DFT phase')
axes[0,1].stem(np.linspace(0,fs,16),np.real(W1))
axes[0,1].set_ylabel('FFT real')
axes[1,1].stem(np.linspace(0,fs,16),np.angle(W1))
axes[1,1].set_ylabel('FFT phase')
for i in range(2):
    for j in range(2):
        axes[i,j].set_xlabel('n')
plt.savefig('CB.EN.U4ECE18248_4.png')
