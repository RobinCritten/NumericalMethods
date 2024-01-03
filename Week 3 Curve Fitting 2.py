# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:59:57 2023

@author: robcr
"""

import numpy as np
import matplotlib.pyplot as plt

def q1():
    x = []
    for i in range(9,174):
        x.append(3*(i**3))
    sumx = summation(x)
    print(sumx)
    
def summation(n):
    sumn = 0
    for i in n:
        sumn+=i
    return sumn

def exercise1():
    
    #create x coords
    xi = np.zeros(11)
    for i in range(1,12):
        xi[i-1] = i  

    #cereate y coords
    yi = np.zeros(11)
    for i in range(1,12):
        yi[i-1] = 2*i + 0.3
        
    A = np.zeros((3,3))
    b = np.zeros(3)

    for i in range(1,12):
        A[0,0] += xi[i-1]**0
        A[0,1] += xi[i-1]**1
        A[0,2] += xi[i-1]**2
        A[1,0] += xi[i-1]**1
        A[1,1] += xi[i-1]**2
        A[1,2] += xi[i-1]**3
        A[2,0] += xi[i-1]**2
        A[2,1] += xi[i-1]**3
        A[2,2] += xi[i-1]**4
    
    

    for i in range(1,12):
        b[0] += (xi[i-1]**0)*yi[i-1]
        b[1] += (xi[i-1]**1)*yi[i-1]
        b[2] += (xi[i-1]**2)*yi[i-1]

    augA = np.copy(A)
    augb = np.copy(b)
    a = gaussJordanElimination(augA, augb, 3)
    print(a)        
    
    #plt.plot(xi,yi)
    #plt.scatter(xi,yi)   

    ymodel = a[0] + a[1]*xi + a[2]*xi**2
       
    plt.figure("Standard")
    plt.plot(xi,yi)
    
    plt.figure("fancy")
    plt.plot(xi,ymodel)
    plt.scatter(xi, yi)

def gaussJordanElimination(augA,augb,n):
    
    #gauss - Jordan elimination nxn
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
    #q1()
    exercise1()
    

if __name__ == "__main__":
    main()