import numpy as np
import matplotlib.pyplot as plt

#P is the limit of the binaomial distribution for low probability of sucess and large number of trail
#.....: timing of the event is indipendent from timing of prevviuos one
# Parameters are:
# lamb= average number of occurence (number of busses)
# dt= time interval in which event can occurance (in 1hr)

def PoissonProcessPath(numOfPaths, numOfSteps,T,lamb):
    X = np.zeros([numOfPaths, numOfSteps+1])
    time =np.zeros([numOfSteps+1])
    dt = T/float(numOfSteps)
    z = np.random.poisson(lamb*dt,[numOfPaths, numOfSteps])
    for i in range(0,numOfSteps):
        X[:,i+1] = X[:,i] + z[:,i]
        time[i+1]=time[i]+dt
        # print("time: ", time)
        # print("dt: ",dt)
        # print("lamb: ", lamb)
        # print("lamb *  dt: ", lamb*dt)
        # print('----------------')

    paths = {"time": time, "X":X}
    return paths

def PoissonProcessPath_Compressed(numOfPaths, numOfSteps,T,lamb):
    Xc = np.zeros([numOfPaths, numOfSteps+1])
    time =np.zeros([numOfSteps+1])
    dt = T/float(numOfSteps)
    z = np.random.poisson(lamb*dt,[numOfPaths, numOfSteps])
    for i in range(0,numOfSteps):
        Xc[:,i+1] = Xc[:,i] - lamb*dt + z[:,i]
        time[i+1]=time[i]+dt
    pathsC = {"time": time, "XCompr":Xc}
    return pathsC


def mainCalc():
    numOfPaths = 25
    numOfSteps = 100
    T = 30
    lamb = 1

    Paths = PoissonProcessPath(numOfPaths, numOfSteps,T,lamb)
    timeGrid = Paths["time"]
    X = Paths["X"]
    PathsC = PoissonProcessPath_Compressed(numOfPaths, numOfSteps,T,lamb)
    timeGridC = PathsC["time"]
    Xc = PathsC["XCompr"] 

    plt.figure("Poisson Process")
    plt.plot(timeGrid, np.transpose(X), '-b')
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel('X(t)')

    plt.figure("Poisson Process Compressed")
    plt.plot(timeGridC, np.transpose(Xc), '-b')
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel('Xc(t)')

    plt.show()

mainCalc()




# def PoissonProcessCompressedPath(numOfPaths, numOfSteps,T,lamb):
#     # We remove mean so the process becomes a martingale
#     Xc =np.zeros([numOfPaths, numOfSteps+1])
#     time =np.zeros([numOfSteps+1])
#     dt = T/float(numOfSteps)
#     z = np.random.poisson(lamb*dt,[numOfPaths, numOfSteps+1])
#     for i in range(0,numOfSteps+1):
#         Xc[:,i+1] = Xc[:,i] - lamb*dt + z[:,i]




