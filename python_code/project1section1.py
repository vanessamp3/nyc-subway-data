"""
Project 1
Section 1. Statistical Test
Improved data set

@author: Vanessa Palzes
@date: 1/11/2015
"""

import pandas as pd
#from mann_whitney_plus_means import mann_whitney_plus_means
import numpy as np
import scipy
import scipy.stats
import random

def mann_whitney_plus_means(turnstile_weather):
    """This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data."""
    
    with_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==1]
    print "Num timepoints with rain = %d" %(len(with_rain))
    
    without_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==0]
    print "Num timepoints without rain = %d" %(len(without_rain))
    
    # Get random indices so that our groups have equal numbers of data points
    random.seed(1)
    without_rain = random.sample(without_rain, len(with_rain))
    print "New num timepoints without rain = %d" %(len(without_rain))
    
    with_rain_mean = np.mean(with_rain)
    without_rain_mean = np.mean(without_rain)
    
    with_rain_normal = scipy.stats.mstats.normaltest(with_rain)
    without_rain_normal = scipy.stats.mstats.normaltest(without_rain)
    print with_rain_normal, without_rain_normal
    
    [U, p] = scipy.stats.mannwhitneyu(with_rain,without_rain)
    
    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader

def printResults(with_rain_mean, without_rain_mean, U, p):
    print "With rain mean = %d" %(with_rain_mean)
    print "Without rain mean = %d" %(without_rain_mean)
    print "U = %d" %(U)
    print "Two-tailed p = %0.8f" %(2*p)

if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename)
    with_rain_mean, without_rain_mean, U, p = mann_whitney_plus_means(turnstile_master)

    printResults(with_rain_mean, without_rain_mean, U, p)