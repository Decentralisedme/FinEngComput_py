
import numpy as np
import matplotlib.pyplot as plt
import scripts
"""
Martingale classifies time series trands and a stochastic process behaves as:
- a martingale if its trajectories display no trends
- submartingale: on average increases
- supermartingasle: on average declines
A Process X = {St; t>0} is martingale if:
- St is known: We know all point up to t
- No exploitment: no jumps
- for all t<T, Et[ST]=St
As conclusion we can say:
- Expectation of Tomorrow is equal to today's value
- Processes need to be driftless: We need move from P to Q measure: from μ to r
- TEST: 
IF E[ST*e^(-T)] = St: Then Process is a martingale
"""
# Reference:
# - Salih N. Neftci: Anintroduction to the Mathemtics of Finalcial Derivatives45
# - Lech Grzelak: Computetional Finance Course: https://www.youtube.com/watch?v=MhmZaHWGWHc&list=PL6zzGYGhbWrPaI-op1UfNl0uDglxdkaOB&index=4

#Parameters
numPaths = int(input("Input Number of Paths:")) #1000
numSteps = int(input("Input Number of Steps:")) #500
# numPaths = 1000
# numSteps = 500

S_0 = 100.00
r = 0.05 #float(input("Input mean:"))
sig = 0.4 #float(input("Input Vol:"))
T = 1

#Genertes the paths
Paths = scripts.generate_paths_GBM_ABM(numPaths,numSteps,T,r,sig,S_0) 

def mainCal():
    M= lambda r,t: np.exp(r*t)
    timeGride =Paths["time"]
    X=Paths["X"]
    S=Paths["S"]

    # plt.figure("GBM Paths")
    # plt.plot(timeGride, np.transpose(X))
    # plt.grid()
    # plt.xlabel("Time")
    # plt.ylabel("X(t)")
    # plt.show()

    ES = np.mean(S[:,-1])
    print("Expected Value for S(T): ",ES)
    
    ESM = np.mean(S[:,-1]/M(r,T))
    print("Discounted Expected Value for S(t): ", ESM)

mainCal()