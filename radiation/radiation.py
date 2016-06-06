import math
d = 5.67*10**(-8)
def findFlow(epsilon,T,A):
    flow = epsilon*(T**4)*d*A
    return flow
def findEpsilon(flow,T,A):
    epsilon = flow/(A*d*T**4)
    return epsilon
def findA(flow,epsilon,T):
    A = flow/(epsilon*d*T**4)
    return A
def findT(flow,epsilon,A):
    T = math.pow(flow/(epsilon*A*d), 1.0/4)
    return T
