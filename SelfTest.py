# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:05:20 2023

@author: robcr
"""
import numpy as np
import matplotlib.pyplot as plt

def sumofthereciprocalsofthesquarenumbers():
    s = 0
    for i in range(1,1000000):
        s += 1/i**2
    print(s)
    
def sumofthereciprocalsofthefactorials():
    s = 0
    for i in range(1,20):
        s += 1/np.math.factorial(i)
    print(s)
    
def matrixmult1():
    A = np.array([[-1/4,1,1,1],[1,-1/4,1,1],[1,1,-1/4,1],[1,1,1,-1/4]])
    b = np.array([4,0,0,4])
    
    print(np.matmul(A,b)) 
    
def matrixmult2(n):
    #n = 10
    A = np.array([[-1/n,1,1,1],[1,-1/n,1,1],[1,1,-1/n,1],[1,1,1,-1/n]])
    b = np.array([n,0,0,n])
    
    a = gaussJordanElimination(A, b, 4)
    
    print(a)
    
    

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

def curvefitting1():
    x = np.linspace(0,10,20)
    y = 2 + 5*x + np.random.normal(size=20)
    
    Z = np.zeros((20,2))
    Z[:,0] = 1
    Z[:,1] = x[:]
    ZT = Z.transpose()
    ZTZ = np.matmul(ZT,Z)
    ZTy = np.matmul(ZT,y)
    
    augZTZ = np.copy(ZTZ)
    augZTy = np.copy(ZTy)
    a = gaussJordanElimination(augZTZ, augZTy, 2)   
    ymodel = np.zeros((20))
    ymodel = a[0] + a[1]*x
    
    plt.figure("Second")
    plt.plot(x,ymodel)
    plt.scatter(x,y);
    
def curvefitting2():
    
    A = np.zeros((6,6))
    b = np.zeros(6)
    
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
    
    for i in x:
        A[0,0] += i**0
        A[0,1] += i**1
        A[0,2] += i**2
        A[0,3] += i**3
        A[0,4] += i**4
        A[0,5] += i**5
        
        A[1,0] += i**1
        A[1,1] += i**2
        A[1,2] += i**3
        A[1,3] += i**4
        A[1,4] += i**5
        A[1,5] += i**6
        
        A[2,0] += i**2
        A[2,1] += i**3
        A[2,2] += i**4
        A[2,3] += i**5
        A[2,4] += i**6
        A[2,5] += i**7
        
        A[3,0] += i**3
        A[3,1] += i**4
        A[3,2] += i**5
        A[3,3] += i**6
        A[3,4] += i**7
        A[3,5] += i**8
        
        A[4,0] += i**4
        A[4,1] += i**5
        A[4,2] += i**6
        A[4,3] += i**7
        A[4,4] += i**8
        A[4,5] += i**9
        
        A[5,0] += i**5
        A[5,1] += i**6
        A[5,2] += i**7
        A[5,3] += i**8
        A[5,4] += i**9
        A[5,5] += i**10
    
    

    for i in range(20):
        b[0] += (x[i]**0)*y[i]
        b[1] += (x[i]**1)*y[i]
        b[2] += (x[i]**2)*y[i]
        b[3] += (x[i]**3*y[i])
        b[4] += (x[i]**4*y[i])
        b[5] += (x[i]**5*y[i])
        
    print("A",A)
    print("b",b)

    augA = np.copy(A)
    augb = np.copy(b)
    a = gaussJordanElimination(augA, augb, 6)
    
    ymodel = a[0] + a[1]*x + a[2]*x**2 + a[3]*x**3 + a[4]*x**4 + a[5]*x**5
    
    plt.figure("Quartic")
    plt.plot(x,y)
    
    plt.figure("Quintic")
    plt.plot(x,ymodel)
    plt.scatter(x, ymodel)




def main():
    #sumofthereciprocalsofthesquarenumbers()
    #sumofthereciprocalsofthefactorials()
    #matrixmult1()
    #matrixmult2(10)
    #matrixmult2(100)
    #matrixmult2(1000)
    #curvefitting1()
    curvefitting2()
    

if __name__ == "__main__":
    main()