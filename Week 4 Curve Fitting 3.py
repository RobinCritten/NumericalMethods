# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:55:54 2023

@author: robcr
"""

import numpy as np
import matplotlib.pyplot as plt

def generalLeastSquares():
    
    x = np.array([10.00,16.30,23.00,27.50,31.00,35.60,39.00,
         41.50,42.90,45.00,46.00,45.50,46.00,49.00,50.00])
    
    
    y = np.array([8.953,16.405,22.607,27.769,32.065,35.641,38.617,41.095,
         43.156,44.872,46.301,47.490,48.479,49.303,49.988])

    Z = np.zeros((15,2))
    Z[:,0] = 1
    Z[:,1] = x[:]
    ZT = Z.transpose()
    ZTZ = np.matmul(ZT,Z)
    ZTy = np.matmul(ZT,y)
    
    augZTZ = np.copy(ZTZ)
    augZTy = np.copy(ZTy)
    a = gaussJordanElimination(augZTZ, augZTy, 2)   
    ymodel = np.zeros((15))
    ymodel = a[0] + a[1]*x
    
    #print(Z)
    #print(ZT)
    #print(ZTZ)
    #print(ZTy)
    #print(a)
    
    #plt.plot(x,y)
    plt.scatter(x,y)
    #plt.scatter(x,ymodel)
    plt.plot(x,ymodel)

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
    generalLeastSquares()
    

if __name__ == "__main__":
    main()