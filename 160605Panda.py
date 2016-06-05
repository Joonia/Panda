# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 13:49:34 2016

@author: klocek
"""
import csv
import numpy

path = "C:\\Users\\Jola\\Documents\\GitHub\\Panda\\Misch-d_1_BA.csv"

#reader=csv.reader(open(path,"rb"),delimiter=',')
#x=list(reader)
#Thk=x[16:19]
#TW=x[20:23]
#MW=x[25:28]

#result=numpy.array(x).astype('float')

#result=numpy.array(list(csv.reader(open("L:\\ale\\substrate_core\\35 Etching Trials\\Misch-d\\Misch-d_1_BA.csv","rb"),delimiter=','))).astype('float')

import pandas as pd
df = pd.read_csv(path)
#saved_column = df['T4_Thk(um)'] #you can also use df['column_name']
#saved_column2 = df['T4_TW(um)'] 
#saved_column3 = df['T3_TW(um)'] 
#saved_column4 = df['T2_TW(um)'] 
#saved_column5 = df['T1_TW(um)'] 
Thk=df.ix[:,'T1_Thk(um)':'T4_Thk(um)']
Thk['median'] = Thk.median(axis=1)

Twid=df.ix[:,'T1_TW(um)':'T4_TW(um)']
Twid['median'] = Twid.median(axis=1)

middleW=df.ix[:,'T1_MW(um)':'T4_MW(um)']
middleW['median'] = middleW.median(axis=1)

bottomW=df.ix[:,'T1_BW(um)':'T4_BW(um)']
bottomW['median'] = bottomW.median(axis=1)

import glob
glob.glob('/Misch-d_*.csv')

path =r'C:\\Users\\Jola\\Desktop\\PYTHON' # use your path
allFiles = glob.glob(path + "/Misch-d_*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
MischD = pd.concat(list_)


Thk=MischD.ix[:,'T1_Thk(um)':'T4_Thk(um)']
Thk['median'] = Thk.median(axis=1)

Twid=MischD.ix[:,'T1_TW(um)':'T4_TW(um)']
Twid['median'] = Twid.median(axis=1)

middleW=MischD.ix[:,'T1_MW(um)':'T4_MW(um)']
middleW['median'] = middleW.median(axis=1)

bottomW=MischD.ix[:,'T1_BW(um)':'T4_BW(um)']
bottomW['median'] = bottomW.median(axis=1)

median = Twid['median']

medianLenght = len(median)

medianSliced = []
medianSlicedLow = []
medianSlicedHigh = []

for i in xrange(0,medianLenght,4):
    medianSliced.append(median[i:4+i])

for i in range(0,len(medianSliced)):
    if i % 2 == 0:
        medianSlicedLow.append(medianSliced[i])
    else:
        medianSlicedHigh.append(medianSliced[i])
