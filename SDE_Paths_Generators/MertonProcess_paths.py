import numpy as np
import matplotlib.pyplot as plt

def MertonPocess_paths_gen(S_0,numPaths,numSteps,lamb,T,mu_j,sig_j,r,sig):
    # Matrices
    X=np.zeros([numPaths,numSteps+1])
    S= np.zeros([numPaths,numSteps])
    # Starting values
    X[:,0]=np.log(S_0)
    S[:0]=S_0
    # Time
    time = np.zeros([numSteps+1])
    dt = T/float(numSteps)
    # Expectation of e^J
    EeJ= np.exp(mu_j + 0.5*sig_j*sig_j)
    # Increments for Poisson and Diffusion Process + J = jump  size with Norm Distr
    Z_poiss = np.random.poisson(lamb*dt, [numPaths,numSteps])
    Z = np.random.normal(0.0, 1.0,[numPaths,numSteps])
    J = np.random.normal(mu_j,sig_j,[numPaths,numSteps])

    for i in range(0,numSteps):
        if numPaths > 1:
            # Z Stabdardisation
            Z[:,i] = (Z[:,i] - np.mean(Z[:,i]))/np.std(Z[:,i])
        # Dynamic for X
        X[:,i+1] = X[:,i] + (r + lamb*dt*EeJ - 0.5*sig*sig)*dt + sig*np.power(dt,0.5)*Z[:,i] + J[:,i]*Z_poiss[:,i]
        time[i+1] = time[i] + dt

    S = np.exp(X)
    paths = {"time": time, "X":X, "S":S}
    return paths

def MainCalc():    
    # Parameters:
    # mu_j and sig_j should celibrated using opt prices in the market
    mu_j = 0.00
    sig_j = 1.20
    r = 0.05
    sig = 0.2
    lamb = 1.00
    S_0 = 100.00
    T = 5
    numPaths = 25
    numSteps = 500
    Paths=MertonPocess_paths_gen(S_0,numPaths,numSteps,lamb,T,mu_j,sig_j,r,sig)
    #print("PATHs: ", Paths)
    timeGrid = Paths["time"]
    X = Paths["X"]
    S = Paths["S"]
           
    plt.figure("Paths: Merton Process for X")
    plt.plot(timeGrid, np.transpose(X))   
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("X(t)")
    
    plt.figure("Paths: Merton Process for S(t)=exp[X(t)]")
    plt.plot(timeGrid, np.transpose(S))   
    plt.grid()
    plt.xlabel("time")
    plt.ylabel("S(t)")
    
    plt.show()

MainCalc()
    



 

