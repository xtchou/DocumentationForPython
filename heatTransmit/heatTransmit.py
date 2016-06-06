def findP(h,A,dt):
    P = h*A*dt
    return P
def findH(P,A,dt):
    h = P/(A*dt)
    return h
def findA(P,h,dt):
    A = P/(h*dt)
    return A
def findDt(P,h,A):
    dt = P/(h*A)
    return dt
