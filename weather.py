#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 9, Part III"""

import urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen('http://www.wunderground.com/history/airport/KNYC/2015/11'
                       '/1/MonthlyCalendar.html?req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=')
bsObj = BeautifulSoup(html)


def main():
    """Parses given wunderground URL and returns days of the month with forecast and/or actual high and low
    temperatures."""
    weather = bsObj.findAll('table', {"class": 'dayTable'})
    for w in weather:
        if w.find('a', {"class": "dateText"}) is None:
            pass
        else:
            day = w.find('a', {"class": "dateText"}).get_text()
        if w.find('td', {"class": "value-header"}, text=['Actual:', 'Forecast:']) is None:
            pass
        else:
            temp_type = w.find('td', {"class": "value-header"}, text=['Actual:', 'Forecast:']).get_text()
            if w.find('span', {"class": "high"}) is None:
                pass
            else:
                high_temp = w.find('span', {"class": "high"}).get_text()[:2]
            if w.find('span', {"class": "low"}) is None:
                pass
            else:
                low_temp = w.find('span', {"class": "low"}).get_text()[:2]
            print "Day of Month: {}, Temp Type: {}, High: {}, Low: {}".format(day, temp_type, high_temp, low_temp)

if __name__ == '__main__':
    main()