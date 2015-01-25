"""
Project 1
Section 2. Linear Regression
Improved data set

@author: Vanessa Palzes
@date: 1/11/2015
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def normalize_features(array):
   """ Normalize the features in the data set. """
   array_normalized = (array-array.mean())/array.std()
   #mu = array.mean()
   #sigma = array.std()

   return array_normalized

def predictions(weather_turnstile):
    """ Estimate coefficients and make predictions using OLS. """
    
    # Features
    X = weather_turnstile[['hour', 'tempi']]
    X = normalize_features(X)
    
    # Add rain to featuers using dummy variables
    #dummy_units = pd.get_dummies(weather_turnstile['rain'], prefix='rain')
    #X = X.join(dummy_units)
    
    # Add conds to featuers using dummy variables
    dummy_units = pd.get_dummies(weather_turnstile['conds'], prefix='conds')
    X = X.join(dummy_units)
    
    #print weather_turnstile['conds'].unique()
    
    # Add day_week to featuers using dummy variables 
    dummy_units = pd.get_dummies(weather_turnstile['day_week'], prefix='day_week')
    X = X.join(dummy_units)    
    
    # Add UNIT to features using dummy variables
    dummy_units = pd.get_dummies(weather_turnstile['UNIT'], prefix='unit')
    X = X.join(dummy_units)
    
    # Add a constant
    X = sm.add_constant(X)    
    
    # Values
    Y = weather_turnstile['ENTRIESn_hourly']
    
    model = sm.OLS(Y, X)
    results = model.fit()
    theta = results.params
    pd.set_option('display.max_rows',len(theta))
    print theta
    
    prediction = np.dot(X,theta)
    
    return prediction

def compute_r_squared(data, predictions):
    """ Compute R2 based on the predictions made in the model. """
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-np.mean(data))**2).sum()
    r_squared = SSReg / SST

    return r_squared

def plot_residuals(turnstile_weather, predictions):
    """ Plots the residuals of the model, so we can see how our model performed. """
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins=30)
    plt.ylabel('Relative Frequency')
    plt.xlabel('Residuals')
    plt.title('Residual Plot')
    return plt

if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values) 

    print "R2 = %f" %r_squared
    
    plot_residuals(turnstile_master, predicted_values)
    