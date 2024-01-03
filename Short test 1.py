# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:46:25 2023

@author: robcr
"""

import numpy as np
import matplotlib.pyplot as plt

def q1():
    x = []
    for i in range(1,198):
        x.append(8*(i**3))
    sumx = summation(x)
    print(sumx)
    
def summation(n):
    sumn = 0
    for i in n:
        sumn+=i
    return sumn

def q2():
    
    #create x coords
    xi = np.zeros(29)
    xi[0] = -10.000000 
    xi[1] = -9.285714 
    xi[2] = -8.571429 
    xi[3] = -7.857143
    xi[4] = -7.142857 
    xi[5] = -6.428571 
    xi[6] = -5.714286 
    xi[7] = -5.000000
    xi[8] = -4.285714
    xi[9] = -3.571429
    xi[10] = -2.857143 
    xi[11] = -2.142857
    xi[12] = -1.428571 
    xi[13] = -0.714286 
    xi[14] = 0.000000 
    xi[15] = 0.714286 
    xi[16] = 1.428571 
    xi[17] = 2.142857 
    xi[18] = 2.857143
    xi[19] = 3.571429
    xi[20] = 4.285714 
    xi[21] = 5.000000 
    xi[22] = 5.714286
    xi[23] = 6.428571
    xi[24] = 7.142857
    xi[25] = 7.857143 
    xi[26] = 8.571429 
    xi[27] = 9.285714 
    xi[28] = 10.000000 

    #cereate y coords
    yi = np.zeros(29)
    yi[0] = 352.726006
    yi[1] = 307.526490
    yi[2] = 264.591054
    yi[3] = 228.662837
    yi[4] = 189.100827
    yi[5] = 157.386374
    yi[6] = 127.589752
    yi[7] = 100.869277
    yi[8] = 79.878626
    yi[9] = 59.982250
    yi[10] = 43.236239
    yi[11] = 26.306277
    yi[12] = 15.893907
    yi[13] = 6.148068
    yi[14] = 3.911111
    yi[15] = -1.246264
    yi[16] = 0.732650
    yi[17] = 4.375860
    yi[18] = 14.550661
    yi[19] = 21.341070
    yi[20] = 36.668980
    yi[21] = 51.966885
    yi[22] = 71.532848
    yi[23] = 93.510004
    yi[24] = 121.960469
    yi[25] = 147.838922
    yi[26] = 179.145222
    yi[27] = 214.114948
    yi[28] = 253.068358
        
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
       
    #plt.plot(xi,yi)
    plt.plot(xi,ymodel)
    plt.scatter(xi, ymodel)

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
    q1()
    q2()
    

if __name__ == "__main__":
    main()