import numpy as np
import matplotlib.pyplot as plt

def exercise1():
    x = np.linspace(0,10)
    y = np.sin(x)
    plt.plot(x,y)
    
def exercise2():
    
    x = []
    for i in range(0,100):
        x.append(2*(i**2))
    sumx = summation(x)
    print(sumx)
        
    x = []
    for i in range(1,101):
        x.append(i)
    sumx = summation(x)
    print(sumx)
    
    x = []
    for i in range(2,201):
        x.append(2*i)
    sumx = summation(x)
    print(sumx)
    
def summation(n):
    sumn = 0
    for i in n:
        sumn+=i
    return sumn

def exercise3():
    x = [ 
    0.526993994,
    0.691126852,
    0.745407955,
    0.669344512,
    0.518168748,
    0.291558862,
    0.010870453,
    0.71818573,
    0.897190954,
    0.476789102,
    ]
    
    y = [
    3.477982975,
    4.197925374,
    4.127080815,
    3.365719179,
    3.387060084,
    1.829099436,
    0.658137249,
    4.023164612,
    5.074088869,
    2.752890033,
    ]
    
    n = 10
    sumx = summation(x)
    sumy = summation(y)  
    xy = []
    for i in range(len(x)):
        xy.append(x[i]*y[i])
    sumxy = summation(xy)    
    xsquare = []
    for i in x:
        xsquare.append(i**2)
    sumxsquare = summation(xsquare)
    
    a1 = ((n * sumxy) - (sumx * sumy)) / ((n * sumxsquare) - (sumx ** 2))
    a0 = (sumy / n) - (a1 * (sumx / n))
    
    print("y =", str(a0), "+", str(a1), "x" )
        
    
def main():
    exercise1()
    exercise2()
    exercise3()
    
if __name__ == "__main__":
    main()

