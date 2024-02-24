import numpy as np
import matplotlib.pyplot as plt
import scripts

"""
P-measure: probability from real historical data where expected returns = μ
Q-measure: risk-neutral probability where expected return = r (risk-free rate) 
"""

#Parameters
numPaths = 50
numSteps = 20
S_0 = 1.00
r = 0.05 #float(input("Input mean:"))
mu = 0.15
sig = 0.1 #float(input("Input Vol:"))
T = 10
M= lambda t: np.exp(r*t)
#Genertes the paths

def mainCal():
    Paths_Q = scripts.generate_paths_GBM_ABM(numPaths,numSteps,T,r,sig,S_0) 
    S_Q=Paths_Q["S"]
    Paths_P = scripts.generate_paths_GBM_ABM(numPaths,numSteps,T,mu,sig,S_0)
    S_P=Paths_P["S"]

    timeGride =Paths_Q["time"]
    # Discouted Paths
    S_P_Ds = np.zeros([numPaths,numSteps+1])
    S_Q_Ds = np.zeros([numPaths, numSteps+1])
    # New Mertices with Discounted Values
    for i, ti in enumerate(timeGride):
        S_Q_Ds[:,i] = S_Q[:,i]/M(ti)
        S_P_Ds[:,i] = S_P[:,i]/M(ti)
        # print(S_P[:,i],M(ti))

    plt.figure("P-Measure: Stock growing at rate mu")
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel("S(t)")
    eSM_P = lambda t: S_0*np.exp(mu*t)/M(t)
    plt.plot(timeGride, eSM_P(timeGride), 'r--')
    plt.plot(timeGride, np.transpose(S_P_Ds),'blue')
    plt.legend(['E^P[S(t)/M(t)]','paths S(t)/M(t)'])

    plt.figure("Q-Measure: Stock growing at rate r")
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel("S(t)")
    eSM_Q = lambda t: S_0*np.exp(r*t)/M(t)
    plt.plot(timeGride, eSM_Q(timeGride), 'r--')
    plt.plot(timeGride, np.transpose(S_Q_Ds),'blue')
    plt.legend(['E^Q[S(t)/M(t)]','paths S(t)/M(t)'])
    
    plt.show()
mainCal()


