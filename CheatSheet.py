#Numerical Methods Cheat Sheet

#######################################################
import numpy as np
import matplotlib.pyplot as plt
import math
#######################################################




#######################################################
def Summation():  
    sumx = 0
    a = 0
    b = 101
    for x in range(a,b): #loops between values a and b
        sumx+=(x) #put summation formula here
    print(sumx)
#######################################################




#######################################################
#Ax = b
#only works for nxn matrices, specify n when calling funciton
#A is an nxn matrix
#b and x are nx1 martrices
def gaussJordanElimination(augA,augb,n):
    
    #gauss elimination nxn
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
#######################################################




#######################################################
#linear transformation
#draws line of best fit for a set of points
def generalLeastSquares(x,y):
#parameters include set of x,y points
    
    n = 15 #number of points

    Z = np.zeros((n,2))
    Z[:,0] = 1
    Z[:,1] = x[:]
    ZT = Z.transpose()
    ZTZ = np.matmul(ZT,Z)
    ZTy = np.matmul(ZT,y)
    
    augZTZ = np.copy(ZTZ)
    augZTy = np.copy(ZTy)
    a = gaussJordanElimination(augZTZ, augZTy, 2)   
    ymodel = a[0] + a[1]*x
    
    plt.scatter(x,y)
    plt.plot(x,ymodel)
#######################################################




#######################################################
#polynomial least squares regression
#maps set of points to a polynomial function and draws model
#guess power of function where appropriate
def PLS(x,y,power):
    
    power +=1
    A = np.zeros((power,power))
    b = np.zeros(power)
    
    for i in x:
        for j in range(power):
            for k in range(power):
                A[j,k] += i**(j+k)
                
    for i in range(len(y)):
        for j in range(power):
            b[j] += (x[i]**j)*y[i]
            
    augA = np.copy(A)
    augb = np.copy(b)
    a = gaussJordanElimination(augA, augb, power)
    
    ymodel = 0
    for i in range(power):
        ymodel += a[i]*x**[i]
    
    #polynomial in form:
    #a[0] + a[1]x + a[2]x^2 + ... + a[n]x^n
    print(a)
    
    plt.figure("Original")
    plt.scatter(x,y)
    plt.plot(x,y)
    
    plt.figure("PLS")
    plt.plot(x,ymodel)
    plt.scatter(x, y)
#######################################################




#######################################################
#Find Roots of 1D Equation
#Newton-Raphson
#Bisection/Secant alternative methods
def NewtonsMethod():
    #Example Equation
    #−3.409843x^3+−10.229528x^2+136.393701x+286.426773=0
    
    eps = 1.0E-10 #eror interval, make smaller for root closer to true value
    #check to make sure answer is correct to accpetable limits
    xold = 0 #set to what function equals
    while True:
        xnew = xold - fx(xold)/numericaldfx(xold)
        dx = xnew - xold
        xold = xnew
        if np.sqrt(dx**2) < eps:
            break
    print("Root {}".format(xnew))
    
def fx(x):
    #calculate function
    #change to correct function
    fx = -3.409843*x**3 + -10.229528*x**2 + 136.393701*x + 286.426773 
    return fx

#change sign of delta to find other roots
def numericaldfx(x, deltax = 0.00001):
    #find derivate numerically using finite differences
    dfx = (fx(x+deltax) - fx(x))/deltax 
    return dfx
    
def dfx(x):
    #find differential of function
    #change to correct differential of function
    dfx = -10.229529*x**2 + -20.459056*x + 136.393701
    return dfx
#######################################################




#######################################################
#solve second order differential equation (and plot them)
def ODES():
    #example
    #d2y/dx2 = 7x^2
    ngrid = 101 #sample size
    x = np.linspace(-10,10,ngrid) #interval (change to fit correct interval)
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
    #g(x) = 8exp[-6x^2+84x-294] (example)
    gx = np.zeros(ngrid) #grid to fill with values
    #loop through all values other than first and last
    for n in range(1,ngrid-1): 
        #change to match equation
        gx[n] = (7*x[n]**2)*dx**2 
    #values of y at the ends of the interval
    gx[0] = -2*-2 #yl (change value that isnt -2 to correct y)
    gx[ngrid-1] = -2*-2 #yr (change value that isnt -2 to correct y)
    
    y = np.linalg.solve(d2y,gx) #solve gaussian elimination
    #plot results
    plt.figure("ODES")
    plt.plot(x,y)
    plt.scatter(x,y)
    print(np.min(y)) 
#######################################################




#######################################################    
def fourier():
    #interval (change to correct interval)
    x = np.linspace(-7, 7, 25, endpoint=False) 
    #number of smaples after interval set to highest reasonable value
    fx = np.array([1.0342346929754642, 0.9058817934145839, 0.6914577309923656, 
         0.602250890566332, 0.6791012347660925, 0.7182707420675367, 
         0.4445638698773424, -0.19897135530521104, -0.9067515348594852, 
         -1.1720691050161398, -0.6557194350783466, 0.5277624118573397, 
         1.8455329804966052, 2.6868503805478303, 2.747440333950096, 
         2.171479067687098, 1.3736704362466177, 0.7202026224718344, 
         0.33251071411854377, 0.1342855688072496, 0.03624430996098024, 
         0.05263086621684633, 0.24628739895713728, 0.5896489272395103, 
         0.9157513451054334]) #solutions (may be equation)
       
    dx = x[1]-x[0] #difference between x values on interval
    
    am,bm = mterms(x,fx,dx) #get m terms
    model_fx = model(am, bm, x) #model solution
    #plot solution
    plt.figure("Fourier")
    plt.scatter(x, fx)
    plt.plot(x, model_fx)

def mterms(x,fx,dx):    
    """
    code to gererate first 10 terms of fourier series of fx
    """
    am = []
    bm = []
    for m in range(0,12): #get phi and psi 
    #set range to be less than twice the number of samples
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
        my_integral *= dx/7 #interval range / 2
        bm.append(my_integral)
        
    return am,bm
    
def get_phi_and_psi(m, x):
    #returns phim and psim for a given x and m
    phim = np.cos(m*np.pi*x/7) #interval range / 2
    psim = np.sin(m*np.pi*x/7) #interval range / 2
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
####################################################### 




####################################################### 
if __name__ == "__main__":
    #Summation()
    #generalLeastSquares(x,y)
    x = np.array([-10.00,-8.75,-7.50,-6.25,-5.00,-3.75,-2.50,-1.25,0.00, 	
                 1.25,2.50,3.75,5.00,6.25,7.50,8.75,10.00])	
    y = np.array([-144.751,-115.964,-90.166,-70.397,-50.308,-33.053,
                  -20.457,-11.167,-5.056,-0.759,-1.298,-4.978,-10.111,
                  -19.584,-31.371,-46.854,-65.216])
    power = 2
    #PLS(x,y,power)
    #NewtonsMethod()
    ODES()
    #fourier()