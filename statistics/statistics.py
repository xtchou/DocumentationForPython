import xlrd
import matplotlib.pyplot as plt
import numpy as np
from numpy import polyfit

def readData(fileName):
    excel = xlrd.open_workbook(fileName)
    sheet = excel.sheet_by_index(0)
    data_num = sheet.ncols/2
    dataGroup = []
    for i in range(0,data_num*2,2):
        xy = {'x':[],'y':[]}
        tempx = []
        tempx = sheet.col_values(i)
        j= i+1
        tempy = []
        tempy = sheet.col_values(j)
        xy['x'] = tempx
        xy['y'] = tempy
        dataGroup.append(xy)
    return dataGroup

def processData(dataGroup):
    for i in range(len(dataGroup)):
        xTotal = 0
        yTotal = 0
        tempx = dataGroup[i]['x']
        tempy = dataGroup[i]['y']
        for k in range(len(tempx)):
            xTotal += float(tempx[k])
            yTotal += float(tempy[k])
            tempx[k] = float(tempx[k])
        tempy[k] = float(tempy[k])
        xTotal = xTotal/len(tempx)
        yTotal = yTotal/len(tempy)
        varianceX = 0
        varianceY = 0
        mulXY=0
        for k in range(len(tempx)):
            varianceX += pow(tempx[k]-xTotal,2)
            varianceY += pow(tempy[k]-yTotal,2)
            mulXY+= (tempx[k]-xTotal)*(tempy[k]-yTotal)
        r=mulXY/pow(varianceX*varianceY,0.5)
        print("The average value of the x&y in the "+ str(i)+ " th data is:"+str(xTotal)+" & "+str(yTotal)+
          ", \nand the variance of the x&y corresponding is: "+str(varianceX)+" & "+str(varianceY)+
          "\nand the relevance coefficient is: "+str(r))
        
def fitting(x,y,counter,):
    plt.plot(x,y,'bo')
    a,b = polyfit(x,y,1)
    plt.figure(counter)
    x = np.linspace(1,20,1000)
    y = a*x+b
    plt.plot(x,y)
    



fileName = 'testData.xlsx' 
dg = readData(fileName)
processData(dg)
for i in range(len(dg)):
    fitting(dg[i]['x'], dg[i]['y'], i+1)
plt.show()


    


