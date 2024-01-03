# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:11:19 2023

@author: robcr
"""

import numpy as np
import matplotlib.pyplot as plt

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
    
    plt.scatter(x,y)
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
        
    

def main():
    lagrangeInterpolation(1.7163714480302947)

if __name__ == "__main__":
    main()