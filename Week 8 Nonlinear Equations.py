# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:38:39 2023

@author: robcr
"""

import numpy as np
import matplotlib.pyplot as plt
import math 

def NewtonsMethod():
    #x^3 - cos(x) = 0
    
    eps = 1.0E-7
    xold = 0
    while True:
        xnew = xold - fx(xold)/numericaldfx(xold)
        dx = xnew - xold
        xold = xnew
        if np.sqrt(dx**2) < eps:
            break
    print("Root {}".format(xnew))
    
def fx(x):
    #calculate function
    fx = x**3 - math.cos(x)
    return fx

def numericaldfx(x, deltax = 0.00001):
    #find derivate numerically using finite differences
    dfx = (fx(x+deltax) - fx(x))/deltax
    return dfx
    
def dfx(x):
    #find differential of function
    dfx = 3*(x**2) + math.sin(x)
    return dfx


def main():
    NewtonsMethod()
    
if __name__ == "__main__":
    main()