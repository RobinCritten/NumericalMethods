# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:19:17 2023

@author: robcr
"""
import numpy as np
import matplotlib.pyplot as plt


def fourier():
    x = np.linspace(-7, 7, 25, endpoint=False) #interval
    fx = np.array([1.0342346929754642, 0.9058817934145839, 0.6914577309923656, 
         0.602250890566332, 0.6791012347660925, 0.7182707420675367, 
         0.4445638698773424, -0.19897135530521104, -0.9067515348594852, 
         -1.1720691050161398, -0.6557194350783466, 0.5277624118573397, 
         1.8455329804966052, 2.6868503805478303, 2.747440333950096, 
         2.171479067687098, 1.3736704362466177, 0.7202026224718344, 
         0.33251071411854377, 0.1342855688072496, 0.03624430996098024, 
         0.05263086621684633, 0.24628739895713728, 0.5896489272395103, 
         0.9157513451054334]) #solutions
       
    dx = x[1]-x[0] #difference between x values on interval
    
    am,bm = mterms(x,fx,dx) #get m terms
    model_fx = model(am, bm, x) #model solution
    #plot solution
    plt.figure("Fourier")
    plt.scatter(x, fx)
    plt.plot(x, model_fx)
    
    #print answer to question
    print("am2:{}, bm2:{}, am2/bm2:{}".format(am[2],bm[2],(am[2]/bm[2])))

def mterms(x,fx,dx):    
    """
    code to gererate first 10 terms of fourier series of fx
    """
    am = []
    bm = []
    for m in range(0,12): #get phi and psi terms, 12 < 25/2
        phim, psim = get_phi_and_psi(m, x)
        
        # cos terms
        my_integral = 0
        for datapoint in range(0,len(x)):
            my_integral += phim[datapoint] * fx[datapoint]
        my_integral *= dx/7
        am.append(my_integral)
        
        # sin terms
        my_integral = 0
        for datapoint in range(0,len(x)):
            my_integral += psim[datapoint] * fx[datapoint]
        my_integral *= dx/7
        bm.append(my_integral)
        
    return am,bm
    
def get_phi_and_psi(m, x):
    #returns phim and psim for a given x and m
    phim = np.cos(m*np.pi*x/7) 
    psim = np.sin(m*np.pi*x/7) 
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

def ODES():
    #d2y/dx2 = aexp[−k(x−x0)^2]
    # k=6,a=8,x0=7
    #d2y/dx2 = 8exp[-6(x-7)^2]
    #d2y/dx2 = 8exp[-6x^2+84x-294]
    ngrid = 101 #sample size
    x = np.linspace(6,7,ngrid) #interval
    dx = 1/(ngrid-1) #difference between each x value
        
    # matrix representing the 2nd derivative operator in finite diff approx
    d2y = np.zeros((ngrid,ngrid))
    
    for n in range(1,ngrid-1):
        d2y[n,n] = -2
        d2y[n,n-1] = 1
        d2y[n,n+1] = 1
    d2y[0,0]=-2
    d2y[ngrid-1,ngrid-1] = -2
    
    
    # g(x) is the RHS the inhomogeneous term (bit not dependent on y)
    #g(x) = 8exp[-6x^2+84x-294]
    gx = np.zeros(ngrid) #grid to fill with values
    #loop through all values other than first and last
    for n in range(1,ngrid-1): 
        gx[n] = (8*np.exp(-6*x[n]**2 + 84*x[n] - 294))*dx**2
    gx[0] = -2*2 #yl
    gx[ngrid-1] = -2*2 #yr
    
    y = np.linalg.solve(d2y,gx) #solve gaussian elimination
    #plot results
    plt.figure("ODES")
    plt.plot(x,y)
    plt.scatter(x,y)
    print(np.min(y))  

if __name__ == "__main__": #run code
   fourier() #q2
   ODES() #q1