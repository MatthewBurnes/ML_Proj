import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import getUrls
import GetVals
import csv
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn import neighbors, datasets
from matplotlib.colors import ListedColormap
import math
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn import svm
from ast import literal_eval
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
import heapq
from sklearn.metrics import RocCurveDisplay
from sklearn.preprocessing import LabelBinarizer


def makePrediction(url='', dataArray=[[]]):
    data = pd.read_csv("Brightness_Data_Copy.csv") #load the existing csv into a data variable

    x = data.drop(['ClearSky'], axis=1) #drop the classification column from the dataset 
    urlCol = x['URL'] 
    x = x.drop(['URL'], axis = 1) #drop the url column from the dataset
    # x['90th Percentile'] = literal_eval(x['90th Percentile']) 
    #x = preprocessing.normalize(x, axis=0)
    y = data['ClearSky'] #save the classification column as a variable
    cw = {'Y': 0.9, 'N': 1.5}
    logr = LogisticRegression(class_weight=cw)
    logr.fit(x, y)
    bigDF = pd.DataFrame()
    vals = GetVals.func(url, bigDF)
    res = logr.predict(vals)
    print(res)


makePrediction("https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/150/08/mango-bdr-greenline-20230530-082200.hdf5")


