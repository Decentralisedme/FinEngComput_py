import numpy as np
import matplotlib.pyplot as plt 
import scripts

# Calculation and Plot
def mainCalc():
    # Parameters
    numPaths = 25
    numSteps = 200
    S_0= 100.00
    r = float(input("Input mean:"))
    sig= float(input("Input Vol:"))
    T= 1
    Paths = scripts.generate_paths_GBM_ABM(numPaths, numSteps,T,r,sig,S_0)
    # Paths = GMB_paths_generator(numPaths, numSteps,T,r,sig,S_0)
    TimeGrid = Paths["time"]
    X=Paths["X"]
    S =Paths["S"]

    plt.figure("GBM Paths")
    plt.plot(TimeGrid, np.transpose(X))
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel("X(t)")
    plt.show()

    plt.figure("ABM Paths")
    plt.plot(TimeGrid, np.transpose(S))
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel("S(t)")
    plt.show()


mainCalc()




