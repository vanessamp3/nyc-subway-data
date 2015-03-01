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
import matplotlib.pyplot as plt

def normality_test(turnstile_weather, variable):
    """ Performs a test of normality on the sample of data. """
    
    sample = turnstile_weather[variable]
    normality = scipy.stats.mstats.normaltest(sample)
    
    print "Normality Measures:"
    print "k2 = %0.3f, p = %0.8f\n" %(normality[0], normality[1]) 

def plot_distribution(turnstile_weather, variable, title, filename):
    """ Create plot distribution of entry data. """
    
    data = turnstile_weather[variable]
    
    plt.figure(figsize=(7,5))
    
    data.hist(bins=20, color='green')
    print max(data)   
    
    plt.ylabel('Frequency')
    axes = plt.gca()
    axes.set_ylim([0,25000])
    
    plt.xlabel('Number of Entries')
    axes.set_xlim([0,33000])
    plt.xticks(range(0,33000,1650))
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    plt.title(title)
    
    plt.gcf().subplots_adjust(bottom=0.15)
    
    # Save to png
    plt.savefig(filename + '.eps', format='eps', dpi=900)

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
    
    normality_test(turnstile_master, "ENTRIESn_hourly")
    plot_distribution(turnstile_master, "ENTRIESn_hourly", "Distribution of Entry Data", "../images/entry_distibution")
    
    with_rain_mean, without_rain_mean, U, p = mann_whitney_plus_means(turnstile_master)

    printResults(with_rain_mean, without_rain_mean, U, p)