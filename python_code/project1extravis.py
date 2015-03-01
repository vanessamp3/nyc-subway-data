"""
Project 1
Section 3. Visualization Extra
Improved data set

@author: Vanessa Palzes
@date: 2/28/2015
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def make_scatter_3d(x, y, sizes, title, mycolor, filename):
    """ Create scatterplot of the data with the size of the points influenced
    by another variable. """
    
    plt.figure(figsize=(40,32))
    
    plt.scatter(x, y, s=sizes, c=mycolor)
    
    plt.ylabel('Latitude')
    axes = plt.gca()
    axes.set_ylim([40.54,40.91])
    
    plt.xlabel('Longitude')
    axes.set_xlim([-74.1,-73.73])
    #plt.xticks(range(0,33000,1650))
    #locs, labels = plt.xticks()
    #plt.setp(labels, rotation=45)
    
    plt.title(title)
    
    font = {'size' : 50}
    matplotlib.rc('font', **font)
    plt.tick_params(length=14, width=5, pad=15)
    
    plt.gcf().subplots_adjust(bottom=0.15)
    
    # Save to png
    plt.savefig(filename + '.eps', format='eps', dpi=900)
    
    return plt

def get_avg_data(turnstiles, all_data, hour, weekday):
    """ Calculates the average number of entries at every turnstile for the
    type of day at a given hour."""
    
    avg_data = []    
    
    for t in turnstiles:
        turn_data = all_data[all_data['UNIT']==t]
        
        entries = turn_data["ENTRIESn_hourly"][(turn_data["hour"]==hour) & 
        (turn_data["weekday"]==weekday)]
        
        avg_data += [np.mean(entries)]
        
    return avg_data

if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename)
    
    # Get unique turnstile IDs
    turnstiles = np.unique(turnstile_master['UNIT'])
    
    # Get Latitude and longitude for the turnstile IDs
    latitude = []
    longitude = []
    for t in turnstiles:
        turnstileIDX = np.where(turnstile_master["UNIT"]==t)
        latitude += [turnstile_master["latitude"][turnstileIDX[0][0]]]
        longitude += [turnstile_master["longitude"][turnstileIDX[0][0]]]
    
    # Get average over weekdays
    weekday_entries = get_avg_data(turnstiles, turnstile_master, 20, 1)
    
    # Create scatter plot
    make_scatter_3d(longitude, latitude, weekday_entries, 
    'Average Entries on Weekdays at Hour 20', '#FF9933', '../images/entry_locations_wkday')
    
    # Get average over weekeneds
    weekend_entries = get_avg_data(turnstiles, turnstile_master, 20, 0)
    
    # Create scatter plot
    make_scatter_3d(longitude, latitude, weekend_entries, 
    'Average Entries on Weekends at Hour 20', '#00CC99', '../images/entry_locations_wkend')
