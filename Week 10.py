# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:32:29 2023

@author: robcr
"""

#phi,psi
import numpy as np
import matplotlib.pyplot as plt


def Orthogonal():
    x = np.linspace(-np.pi, np.pi, 10, endpoint=False) #10 random values of x
    
    dx = x[1] - x[0]
    
    m = 5
    phim = np.cos(m*np.pi*x/np.pi) 
    psim = np.sin(m*np.pi*x/np.pi) 
    
    plt.figure("Orthogonal")
    plt.plot(x, phim)
    plt.plot(x, psim)
    
    """
    code to do numerical integration using trapezium rule
    Because first and last points (0 and 2l) are the same we can just add the point at 0 and ignore factors of 1/2
    """
    my_integral = 0
    for datapoint in range(0,len(x)):
        my_integral += psim[datapoint] * phim[datapoint]
    my_integral *= dx

def fourier():
    x = np.linspace(-np.pi, np.pi, 20, endpoint=False)
    dx = x[1]-x[0]
    #fx = np.cos(x) + 0.5*np.cos(2*x) + 0.25*np.sin(3*x)
    #fx = np.cos(x)
    fx = np.cos(x) + np.cos(2*x)
    
    am,bm = mterms(x,fx,dx)
    model_fx = model(am, bm, x)
    plt.scatter(x, fx)
    plt.plot(x, model_fx)

def mterms(x,fx,dx):    
    """
    code to gererate first 10 terms of fourier series of fx
    """
    am = []
    bm = []
    for m in range(0,10):
        phim, psim = get_phi_and_psi(m, x)
        
        # cos terms
        my_integral = 0
        for datapoint in range(0,len(x)):
            my_integral += phim[datapoint] * fx[datapoint]
        my_integral *= dx/np.pi
        am.append(my_integral)
        
        # sin terms
        my_integral = 0
        for datapoint in range(0,len(x)):
            my_integral += psim[datapoint] * fx[datapoint]
        my_integral *= dx/np.pi
        bm.append(my_integral)
        
    return am,bm
    
def get_phi_and_psi(m, x):
    """returns phim and psim for a given x and m"""
    phim = np.cos(m*np.pi*x/np.pi) 
    psim = np.sin(m*np.pi*x/np.pi) 
    return phim, psim

# build our model function to see if it fits the original data
def model(am,bm,x):
    fx = np.zeros(len(x))
    numterms = len(am)
    # do a/0 term first
    
    fx += am[0]/2
    
    # add the a1, b1 ... aN-1, bN-1, terms
    for term in range(1, numterms):
        phim, psim = get_phi_and_psi(term, x)
        fx += am[term]*phim
        fx += bm[term]*psim
        
    return fx

if __name__ == "__main__":
    fourier()
