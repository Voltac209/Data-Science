import os 
os.chdir('C:\\Users\\Raghav Sood\\Documents\\Data Science\\Part 1')
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.impute import SimpleImputer

dataset=pd.read_csv('Data.csv')
x=dataset.iloc[:,:-1].values #.values converts to NumPy array
y=dataset.iloc[:,-1].values 

imputer=SimpleImputer(missing_values=np.nan,strategy='mean') #sets the null values equal to the mean value of the given column
#this imputer also needs to be connected to the matrix of features

imputer.fit(x[:,1:3]) #stores the data that we asked to change 
x[:,1:3]=imputer.transform(x[:,1:3]) #applies changes to the matrix
print(x)