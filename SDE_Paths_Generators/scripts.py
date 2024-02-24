import numpy as np
import matplotlib.pyplot as plt

# Function to generate paths 
"""
Generalised Brownian Motion:
dSt = alpha(S,t)dt + sigma(S,t)dWt

ABM SDE:
IF alpha(S,t) as μ and sigma are constant
S price will move indipendantly to current S price
--- dSt = μdt + sigma dWt

GBM SDE:
Add a stochastic process which is proportional to current level S
--- dSt = μ S dt + sigma S dWt
Devide by S and you have % change of S which is Norm Distrib
dSt/S ~N(μdt, sigma √(dt))
The relative returns of [(S0-dSt)/S0 =] St/S0 over period of time T is 
the product of price changes: 
- ST/S0 = S1/S0*S2/S1 ...ST/ST-1
Log of the product convert to sum series
- ln(ST/S0) = ln(S1/S0)+ ln(S2/S1) ...ln(ST/ST-1)
This a the base of motivation for lognormal diffusion stochastic differential equation
Two dimansions:
- Time: dt
- Probabiity: dW
"""
# Reference:
# - John Wiley:  https://catalogimages.wiley.com/images/db/pdf/9781118487716.excerpt.pdf
# - LechGrzelak: Computetional Finance Course:https://www.youtube.com/watch?v=MhmZaHWGWHc&list=PL6zzGYGhbWrPaI-op1UfNl0uDglxdkaOB&index=4

def generate_paths_GBM_ABM(numPaths,numSteps,T,r,sig,S_0):
    # Zero Metrices:
    X = np.zeros([numPaths,numSteps+1])
    S = np.zeros([numPaths,numSteps+1])
    time = np.zeros([numSteps+1])

    # Diffuzion Process dWt = Z ~N(0,1) Matrice
    Z = np.random.normal(0.0,1.0,[numPaths,numSteps]) 

    #Starting values:
    X[:,0] = np.log(S_0)
    # Time dt
    dt = float(T/numSteps)

    for i in range(0,numSteps):
        if numPaths >1:
            Z[:,i] = (Z[:,i] - np.mean(Z[:,i])) / np.std(Z[:,i])
        
        # # Discretization:
        ## X(t+1) = X(t) + (u - (sig^2)/2)d(t) + sig((e^0.5(dt))*Z) 
        X[:,i+1] = X[:,i] + (r -0.5*(sig**2))*dt + sig*(np.sqrt(dt))*Z[:,i]
        time[i+1] = time[i] + dt
    
    #ABM
    S = np.exp(X)
    paths = {"time":time, "X":X, "S":S}
    return paths









