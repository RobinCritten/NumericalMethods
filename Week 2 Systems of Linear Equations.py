# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:04:01 2023

@author: robcr
"""
import numpy as np

def gaussElimination():
    dims = (4,4)
    A = np.zeros(dims)
    A[0,0] = 1
    #print(A[0:3,0:3])
    #print(A[0:1,:]) #A[0:1,0:4]
    row0 = [2,2,4,-2]
    row1 = [1,3,2,4]
    row2 = [3,1,3,1]
    row3 = [1,3,4,2]
    A[0,:] = row0 #A[0,0:4] = row0
    A[1,:] = row1
    A[2,:] = row2
    A[3,:] = row3
    print(A)
    
    b = np.zeros(4)
    b = [10,17,18,27]
    print(b)

    #gauss elimination 4x4
    for i in range(0,3):
        j = i + 1
        while j <= 3:
            m = A[j,i]/A[i,i]
            A[j,0:4] = A[j,0:4] - m*A[i,0:4]
            b[j] = b[j] - m*b[i]
            j+=1
            
    print(A)
    print(b)

def gaussJordanElimination():
    dims = (4,4)
    A = np.zeros(dims)
    A[0,0] = 1
    #print(A[0:3,0:3])
    #print(A[0:1,:]) #A[0:1,0:4]
    row0 = [2,2,4,-2]
    row1 = [1,3,2,4]
    row2 = [3,1,3,1]
    row3 = [1,3,4,2]
    A[0,:] = row0 #A[0,0:4] = row0
    A[1,:] = row1
    A[2,:] = row2
    A[3,:] = row3
    print(A)
    
    b = np.zeros(4)
    b = [10,17,18,27]
    print(b)

    #gauss - Jordan elimination 4x4
    for i in range(0,4):
        j = 0
        while j <= 3:
            if j != i:
                m = A[j,i]/A[i,i]
                A[j,0:4] = A[j,0:4] - m*A[i,0:4]
                b[j] = b[j] - m*b[i]
            j+=1
            
    print(A)
    print(b)
    
    #reduction
    for i in range(0,4):
        b[i] = b[i] / A[i,i]
        A[i,i] = 1
        
    print(A)
    print(b)
    
def main():
    gaussElimination()
    gaussJordanElimination()
    
if __name__ == "__main__":
    main()