# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:00:23 2019

@author: Vipul
"""

# Data Preprocessing
import pandas as pd

dataset = pd.read_csv("Quadratic_Data.csv")
X = dataset.iloc[:,0:3].values
y = dataset.iloc[:,3:].values

# Splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScalar
sc = StandardScalar()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Creating the ANN model
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initializing the model
regressor = Sequential()

def self_activate(x):
    return 0.5*x

# Adding the input layer and the first hidden layer
regressor.add(Dense(output_dim = 9, init = "uniform", activation = "sigmoid", input_dim = 3))

# Adding the output layer
regressor.add(Dense(output_dim = 2, init = "uniform", activation = "sigmoid"))

# Compiling the model
regressor.compile(optimizer = "adam", loss = "mse", metrics = ["accuracy"])

# Fitting the ANN model to the training set
trained_model = regressor.fit(X_train, y_train, batch_size = 32, nb_epoch = 10)

# Predicting the test set results
y_pred = regressor.predict(X_test)
