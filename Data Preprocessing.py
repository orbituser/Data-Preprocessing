# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:34:57 2023

@author: mozea
"""

import pandas as pd


#data = pd.read_csv("STEG_BILLING_HISTORY (1).csv")
dataset = pd.read_csv("STEG_BILLING_HISTORY (1).csv")

client_0_bills = dataset.head(10) #Stored the first ten lines of the dataset in a variable. The data type of the variable is a dataframe

dataset_info = client_0_bills.info()
#Shows the information about the client_0_bills dataset
# It has 10 rows and 16 columns
# There are four columns with categorical features
# The memory usage of the dataset is 1.4+ KB

categorical_columns = client_0_bills.select_dtypes(include = 'object') 
#Returns the columns with categorical features. Uses the keyword 'object' because the column consists of both numerical and categorical data
#In the case of strictly categorical, the keyword will be 'category' and for numerical, the keyword will be the datatype ie 'float64', 'int32'

data_null_count = client_0_bills.isnull().sum() #Checking for any null values in the dataset

#In the case where there are missing values, I will replace those values using some measures of central tendency, depending on whether it is a numerical or categorical column, and in the case of numerical, I will further check to see if it is a normal distribution. However if the number of missing rows in a column are more than 40% of that column, I will drop the column. Comparison of the two datasets can be done to know which is better, and the better one would be selected.

numerical_columns = client_0_bills.select_dtypes(include = ['int64', 'float64'])
data_descriptive_statistic = numerical_columns.describe()

# Bill_records = client_0_bills.loc['train_Client_0'] ---> Didn't work, idk why
Bill_records1 = client_0_bills.loc[:, :] #Selected all the rows with the id = 'train_Client_0' (which happens to be all of them so...I selected them all)

client_0_bills = pd.get_dummies(client_0_bills, columns = ["counter_type"], dtype = int) #Converted the 'counter_type' column to a numerical one

client_0_bills = client_0_bills.drop(["counter_statue"], axis = 1) #Dropped the column 'counter_statue'



