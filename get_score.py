# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:45:30 2021

@author: PC
"""

#模型训练
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import Lasso,LogisticRegression
import numpy as np
from metrics1 import model_parameter
import metrics1 as mp1
from sklearn.preprocessing import label_binarize
#import equal_test
from sklearn.model_selection import train_test_split
import scikitplot as skplt
import joblib
# In[con_log]
def con_log(list):    
    def f(x):
        if x<0.2:
            return(1)
        elif x<0.4:
            return(2)
        elif x<0.6:
            return(3)
        elif x<0.8:
            return(4)
        else:
            return(5)
    return([f(x) for x in list])

# In[]
def get_points(test_x):
    nsclc_model =joblib.load("NSCLC_model.pkl")
    new_predictions = nsclc_model.predict_proba(test_x)[:,1]
    score = con_log(new_predictions)
    print("your score is %s,please refer to the KM plot to review your overall survival probability"%score)
    
    
