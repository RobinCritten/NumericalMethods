# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:19:52 2023

@author: robcr
"""

import numpy as np
import matplotlib.pyplot as plt

def q1():
        
    A = np.zeros((4,4))
    b = np.zeros(4)
    
    x = np.array([-10.000000,
         -8.666667,
         -7.333333, 
         -6.000000, 
         -4.666667, 
         -3.333333, 
         -2.000000, 
         -0.666667,
         0.666667,
         2.000000, 
         3.333333, 
         4.666667, 
         6.000000, 
         7.333333, 
         8.666667, 
         10.000000])
    y = np.array([-236.858690,
         -179.783455,
         -132.915145,
         -92.106830,
         -60.370058,
         -31.857908,
         -10.878956,
         1.061574,
         4.291217,
         3.578033,
         -5.377525,
         -25.148321,
         -45.176053,
         -75.555361,
         -113.610130,
         -156.051823])

    for i in x:
        A[0,0] += i**0
        A[0,1] += i**1
        A[0,2] += i**2
        A[0,3] += i**3
        
        A[1,0] += i**1
        A[1,1] += i**2
        A[1,2] += i**3
        A[1,3] += i**4
        
        A[2,0] += i**2
        A[2,1] += i**3
        A[2,2] += i**4
        A[2,3] += i**5
        
        A[3,0] += i**3
        A[3,1] += i**4
        A[3,2] += i**5
        A[3,3] += i**6
    
    

    for i in range(16):
        b[0] += (x[i]**0)*y[i]
        b[1] += (x[i]**1)*y[i]
        b[2] += (x[i]**2)*y[i]
        b[3] += (x[i]**3*y[i])

    augA = np.copy(A)
    augb = np.copy(b)
    a = gaussJordanElimination(augA, augb, 4)
    print(a)        
    
    #plt.plot(x,y)
    #plt.scatter(x,y)   

    ymodel = a[0] + a[1]*x + a[2]*x**2 + a[3]*x**3
    
    plt.figure("Quadratic")
    plt.plot(x,y)
    
    plt.figure("Cubic")
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

#q2
def lagrangeInterpolation(xinterpolate):
    
    x = np.array([1.0, 2.25, 3.5, 4.75, 6.0])
    
    y = np.array([3.0, 6.75, 10.5, 14.25, 18.0])
    
    total = 0    
    for i in range(len(y)):
        n = numerator(x, xinterpolate, i)
        d = denominator(x, i)
        if d != 0:
            total = total + ((n / d) * y[i])
        
    print("p(x) = ", total)
    
    plt.figure("lagrange")
    plt.scatter(x,y)
    plt.plot(x,y)
            
def numerator(x,xinterpolate,i):
    n = 1
    for counter in range(len(x)):
        if i != counter:
            n = n * (xinterpolate - x[counter])
    return n
            
def denominator(x,i):
    d = 1
    for counter in range(len(x)):
        if i != counter:
            d = d * (x[i]-x[counter])
    return d

def BilinearInterpolation(x,y):
    
    xi = np.array([6,12])
    yi = np.array([6,10])
    T = np.array([7,5,7,5])
    
    Fxy1 = ((xi[1]-x)/(xi[1]-xi[0]))*T[0]+((x-xi[0])/(xi[1]-xi[0]))*T[1]
    Fxy2 = ((xi[1]-x)/(xi[1]-xi[0]))*T[2]+((x-xi[0])/(xi[1]-xi[0]))*T[3]
    print(Fxy1)
    print(Fxy2)
    Fxy = ((yi[1]-y)/(yi[1]-yi[0]))*Fxy1+((y-yi[0])/(yi[1]-yi[0]))*Fxy2
    print("Bilenar Interpolation:",Fxy)
    
        

def main():
    q1()
    lagrangeInterpolation(1.7163714480302947)
    BilinearInterpolation(7.600000,6.400000)
    

if __name__ == "__main__":
    main()