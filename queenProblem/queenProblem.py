from __builtin__ import False
import datetime
QUEENPOSITION = []
N=0

def modify(column,ld,rd,r,c): #column is used to store the collision number in a certain column
    global N  #length of the square
    global QUEENPOSITION  
    #row column,ld rd, used to record the collision on the row, column and diagnol
    collisionNum=0
    collisionNum=collisionNum+column[c]
    collisionNum=collisionNum+ld[r-c+N]-1
    collisionNum=collisionNum+rd[r+c]-1
    minCollisionNum = collisionNum
    bestColumn = c
    for i in range(N):
        costNow = collisionNum+column[i]
        costNow = costNow+ld[r-i+N]-1
        costNow = costNow+ rd[r+i]-1
        if costNow<minCollisionNum:
            minCollisionNum = costNow
            bestColumn = i
    #modify the row now to the best column
    column[c] -=1
    ld[r-c+N] -=1
    rd[r+c]-=1
    column[bestColumn]+=1
    ld[r-bestColumn+N]+=1
    rd[r+bestColumn]+=1
    QUEENPOSITION[r] = bestColumn
    if column[c]==1 and column[bestColumn]==1 and ld[r-bestColumn+N]==1 and rd[r+bestColumn]==1:
        return [check(column,ld,rd)]
    return [False]
def check(column,ld,rd):
    global N
    global QUEENPOSITION
    for i in range(N):
        if column[i]!=1 or ld[i-QUEENPOSITION[i]+N]!=1 or rd[i+QUEENPOSITION[i]]!=1:
            return [False]
    return [True]


import numpy
global N
global QUEENPOSITION
#input N
str = raw_input('Please input an N: ')
N  = int(str)
#begin timing
repeatTimes = 10
totalTime = 0
for k in range(repeatTimes):
    timeBegin = datetime.datetime.now()
    #initialization
    column = numpy.zeros(N)
    ld = numpy.zeros(2*N-1)
    rd = numpy.zeros(2*N-1)
    QUEENPOSITION = numpy.zeros(N)
    temp_list = numpy.random.permutation(range(N))
    for i in range(len(temp_list)):
        QUEENPOSITION[i]=temp_list[i]
        column[temp_list[i]]+=1
        ld[i-temp_list[i]+N]+=1
        rd[i+temp_list[i]]+=1
    mark = True
    if check(column,ld,rd):
        print('Found!\n')
        mark = False

    while mark:
        for i in range(N):
            if modify(column, ld, rd, i, QUEENPOSITION[i]):
                mark = False
                print('Found!\n')
                break
    timeEnd = datetime.datetime.now()
    timeSpent = timeEnd-timeBegin
    totalTime += timeSpent.seconds*1000000+timeSpent.microseconds
print totalTime/repeatTimes       





    
    