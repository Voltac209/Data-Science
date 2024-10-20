import os 
os.chdir('C:\\Users\\Raghav Sood\\Documents\\Data Science\\Part 1')

import pandas as pd
import numpy as np
import matplotlib as plt



dataset = pd.read_csv('Data.csv')
x=dataset.iloc[:,:-1].values ##iloc takes the index of rows and columns  and : signifies complexte range  :-1 takes all the columns except the last one
#X does not contain the dependendent column
#X is matrix of features
y=dataset.iloc[:,-1].values #Y containts the dependent column
#Y is dependent variable vector
print(x)
print(y)
