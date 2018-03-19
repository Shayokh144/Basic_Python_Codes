# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:50:38 2017

@author: Asif
"""
import csv
rd = open("nfl.csv")
data =csv.reader(rd)
listr=list(data)
print(listr[1])
patriots_wins = 0
for item in listr:
    if item[2]=='New England Patriots':
        patriots_wins+=1
print(patriots_wins)        
 
##############################################################################
 
 f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(teamName):
    cnt=0
    for item in nfl:
        if item[2]==teamName:
            cnt+=1
    return cnt

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")

#######################################################################

class Dataset:
    def __init__(self,data):
        self.type = "csv"
        self.data=data
f=open("nfl.csv")
nfl_dataset=csv.reader(f) #read csv file
dsToList=list(nfl_dataset)

datas = Dataset(dsToList)
dataset_data=datas.data


###############################################################################


import csv
rd = open("nfl.csv")
data =csv.reader(rd)
nfl_data = list((data))
print(nfl_data[0])

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
       
    # Add your method here.
    def column (self,label):
       
        if label  not in self.header:
            return None
        else:
            lst=[]
            for idx, value in enumerate(self.header):
                if value==label:
                    for item in self.data:
                        lst.append(item[idx])
            return lst
                    
        
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
print(year_column)
player_column = nfl_dataset.column('player')
##########################################################################

'''
using ___str__ to convert string
'''
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    # Add the special method here
    def __str__(self):
        return str(self.data[:10])
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
        
    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)

