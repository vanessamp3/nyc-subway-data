"""
Project 1
Exploring the data set
Improved data set

@author: Vanessa Palzes
@date: 1/11/2015
"""

import pandas as pd
import datetime
import numpy as np

def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There is a useful function in the datetime library called strptime. 
    More info can be seen here:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''

    dt = datetime.datetime.strptime(date, "%m-%d-%y")
    date_formatted = datetime.date(dt.year, dt.month, dt.day)
    return date_formatted

def printDates(turnstile_weather):
    """This function will print the min and max day of the dataset."""
    
    min_date = reformat_subway_dates(min(turnstile_weather['DATEn']))
    max_date = reformat_subway_dates(max(turnstile_weather['DATEn']))
    
    print min_date.strftime('Min date: %m/%d/%Y')
    print max_date.strftime('Max date: %m/%d/%Y')
    
def printNumUnits(turnstile_weather):
    """This function will print the number of units included in the data set."""
    
    stations = np.unique(turnstile_weather['UNIT'])
    numStations = len(stations)
    print "Num stations: %d" %numStations

if __name__ == "__main__":
    input_filename = "turnstile_weather_v2.csv"
    turnstile_master = pd.read_csv(input_filename)
    
    printDates(turnstile_master)
    printNumUnits(turnstile_master)