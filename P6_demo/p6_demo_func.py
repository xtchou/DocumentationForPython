# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
from  statistics import mean,stdev,pstdev,variance,pvariance

from prettytable import PrettyTable
import glob

filenames=[]

xygroup=[]

xstagroup=[]
ystagroup=[]
rgroup=[]

lfit=[]

def getData_TextFile(fileName):

    dataFile = open(fileName, 'r')

    xy={'x':[],'y':[]}

    discardHeader = dataFile.readline()

    for line in dataFile:
        x,y= line.split()
        xy['x'].append(float(x))
        xy['y'].append(float(y))

    dataFile.close()

    return xy

def satData(x,y):
    xsta={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None}
    ysta={'avg':None,'stdev':None,'pstdev':None,'var':None,'pvar':None}

    xsta['avg']=mean(x)
    ysta['avg']=mean(y)

    xsta['stdev']=stdev(x)
    ysta['stdev']=stdev(y)

    xsta['pstdev']=pstdev(x)
    ysta['pstdev']=pstdev(y)

    xsta['var']=variance(x)
    ysta['var']=variance(y)

    xsta['pvar']=pvariance(x)
    ysta['pvar']=pvariance(y)

    r=np.corrcoef(x,y)[0, 1]

    return  xsta,ysta,r

def fitData(x,y):
    #find linear fit
    a,b = np.polyfit(x,y,1)
    predictedY = a*np.array(x) + b
    return a,b,predictedY

def plotData(x,y,a,b, predictedY,fileName):
    plt.plot(x,y, 'bo',
               label= fileName)

    plt.title(fileName)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(x,predictedY,
               label = 'Y by\nlinear fit, y = '
               + str(round(a, 5))+'*x+'+str(round(b, 5)))

    plt.legend(loc = 'best')

def processing_one_TextFile(filename):

    xy=getData_TextFile(filename)

    xsta,ysta,r=satData(xy['x'],xy['y'])

    a,b,predictedY=fitData(xy['x'],xy['y'])

    return xy,xsta,ysta,r,a,b,predictedY

def processing_data_TextFiles(filenames):

    for i in range(len(filenames)):

        xy,xsta,ysta,r,a,b,predictedY =processing_one_TextFile(filenames[i])

        xygroup.append(xy)

        xstagroup.append(xsta)
        ystagroup.append(ysta)

        rgroup.append(r)

        lfit.append({'a':a,'b':b,'preY':predictedY})

def processing_plot_TextFiles(filenames):

    fig=plt.figure(figsize=(12.0,8.0))

    fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)

    figcount=len(filenames)

    figcol=2
    figrow=math.ceil(figcount/figcol)

    for i in range(figcount):
        fig.add_subplot(figrow, figcol,i+1)
        plotData(xygroup[i]['x'],xygroup[i]['y'],
                 lfit[i]['a'],lfit[i]['b'],lfit[i]['preY'],filenames[i])

    plt.show()

def processing_table_TextFiles(filenames):

    table = PrettyTable(["data set",
                         "x-avg", "x-std", "x-pstd", "x-var","x-pvar",
                         "y-avg", "y-std", "y-pstd", "y-var","y-pvar",
                         "pearson_r"])

    table.align= "r" # right align
    table.padding_width = 1 # One space between column edges and contents (default)

    for i in range(len(filenames)):
        table.add_row([filenames[i],
                   "%.3f" % xstagroup[i]['avg'],
                   "%.3f" % xstagroup[i]['stdev'],"%.3f" %xstagroup[i]['pstdev'],
                   "%.3f" % xstagroup[i]['var'],"%.3f" % xstagroup[i]['pvar'],
                   "%.3f" % ystagroup[i]['avg'],
                   "%.3f" % ystagroup[i]['stdev'],"%.3f" % ystagroup[i]['pstdev'],
                   "%.3f" % ystagroup[i]['var'],"%.3f" % ystagroup[i]['pvar'],
                   "%.3f" % rgroup[i]])
    print(table)

if __name__ == '__main__':

    filenames=glob.glob(r'./Anscombe*.txt')
 
    processing_data_TextFiles(filenames)
    processing_table_TextFiles(filenames)
    processing_plot_TextFiles(filenames)
