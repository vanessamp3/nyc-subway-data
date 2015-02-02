"""
Project 1
Section 3. Visualization, Part 2
Improved data set

@author: Vanessa Palzes
@date: 1/16/2015
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def make_plot(data, title, mycolor, filename):
    """ Creates plot of entries at different hours of the day. """
    
    plt.figure(figsize=(7,5))
    
    plt.bar(data['hour'], data['avg'], width=3, align="center")
    
    plt.ylabel('Average Number of Entries')
    
    plt.xlabel('Hour of the Day (Military)')
    plt.xticks([0, 4, 8, 12, 16, 20])
    plt.title(title)
    
    plt.gcf().subplots_adjust(bottom=0.15)
    
    # Save to png
    plt.savefig(filename + '.eps', format='eps', dpi=900)
    
    return plt

def avg_riders_hourly(turnstile_data):
    """ Calculates the average number of riders for all the hours in a day. """    
    
    hours = np.unique(turnstile_data['hour'])
    stations = np.unique(turnstile_data['UNIT'])
    numStations = len(stations)
    
    avg_riders = np.zeros(len(hours))    
    
    for num, i in enumerate(hours):
        idx = turnstile_data['hour']==i
        data = turnstile_data['ENTRIESn_hourly'][idx]
        data = data.fillna(0)
        total_riders = np.sum(data)
        avg_riders[num] = total_riders/numStations

    avg_hourly = pd.DataFrame({'hour': hours, 'avg': avg_riders})
        
    return avg_hourly

if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename)
    
    # Determine hourly average entries
    avg_hourly = avg_riders_hourly(turnstile_master)
    print avg_hourly
    
    # Plot the data
    print(turnstile_master['hour'])
    make_plot(avg_hourly, 'Average NYC Subway Ridership by the Hour', 'green', 'hourlyhistogram')
    