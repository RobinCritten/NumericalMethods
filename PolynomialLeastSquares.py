# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:13:05 2023

@author: robcr
"""
#code generates polynomial least squares regression plots for two 
#given set of coordinates of the same length and a power of choice
import numpy as np
import matplotlib.pyplot as plt

def PLS(x,y,power):
    
    power +=1
    A = np.zeros((power,power))
    b = np.zeros(power)
    
    for i in x:
        for j in range(power):
            for k in range(power):
                A[j,k] += i**(j+k)
                
    for i in range(len(y)):
        for j in range(power):
            b[j] += (x[i]**j)*y[i]
            
    augA = np.copy(A)
    augb = np.copy(b)
    a = gaussJordanElimination(augA, augb, power)
    
    ymodel = 0
    for i in range(power):
        ymodel += a[i]*x**[i]
    
    plt.figure("Quartic")
    plt.plot(x,y)
    
    plt.figure("Quintic")
    plt.plot(x,ymodel)
    plt.scatter(x, ymodel)
    
#gauss - Jordan elimination nxn
def gaussJordanElimination(augA,augb,n):
    
    for i in range(0,n):
        j = 0
        while j <= n-1:
            if j != i:
                m = augA[j,i]/augA[i,i]
                augA[j,0:n] = augA[j,0:n] - m*augA[i,0:n]
                augb[j] = augb[j] - m*augb[i]
            j+=1
            
    
    #reduction
    for i in range(0,n):
        augb[i] = augb[i] / augA[i,i]
        augA[i,i] = 1
    
    return augb
    
    
def main():
    x = np.array([-10.        ,  -8.94736842,  -7.89473684,  -6.84210526,
        -5.78947368,  -4.73684211,  -3.68421053,  -2.63157895,
        -1.57894737,  -0.52631579,   0.52631579,   1.57894737,
         2.63157895,   3.68421053,   4.73684211,   5.78947368,
         6.84210526,   7.89473684,   8.94736842,  10.        ])
    
    y = np.array([-51.52715788, 110.0527426 , 185.9883986 , 198.15250142,
       171.51661575, 123.4801728 ,  67.44843859,  14.22294276,
       -24.64571893, -46.75244647, -47.45743374, -24.63662458,
        14.4708924 ,  66.32546058, 126.05083546, 172.493118  ,
       200.13810257, 186.35506754, 108.24045324, -50.18592379])
    
    PLS(x,y,10)
    
if __name__ == "__main__":
    main()