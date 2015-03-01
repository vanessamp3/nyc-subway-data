"""
Project 1
Section 3. Visualization, Part 1
Improved data set

@author: Vanessa Palzes
@date: 1/16/2015
@updated: 2/25/2015
"""

import pandas as pd
import matplotlib.pyplot as plt

def make_histogram(data, title, mycolor, filename):
    """ Create histograms of ridership when it is raining and not raining. """
    
    plt.figure(figsize=(7,5))
    
    data.hist(bins=20, color=mycolor)
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
    
    return plt


if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename)
    
    raining = turnstile_master['rain']==1
    notraining = turnstile_master['rain']==0
    
    raindata = turnstile_master['ENTRIESn_hourly'][raining]
    notraindata = turnstile_master['ENTRIESn_hourly'][notraining]    
    
    # Histogram when raining
    make_histogram(raindata, 'NYC Subway Ridership when Raining', 'blue', 'rainhistogram')

    # Histogram when not raining
    make_histogram(notraindata, 'NYC Subway Ridership when not Raining', 'red', 'notrainhistogram')
    