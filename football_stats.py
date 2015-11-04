#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 9, Part I"""

import urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen('http://www.cbssports.com/nfl/stats/'
                       'playersort/nfl/year-2015-season-regular-category-touchdowns')
bsObj = BeautifulSoup(html)

td_table = bsObj.findAll("table", attrs={"class":"data"})[0].findAll('tr', attrs={"valign":"top"})

def main():
    counter = 0
    print "Here are the 20 players currently with the most touchdowns:"
    for i in td_table:
        name = i.findAll('td')[0].findAll('a')[0].contents[0]
        position = i.findAll('td')[1].contents[0]
        team =  i.findAll('td')[2].findAll('a')[0].contents[0]
        tds = i.findAll('td')[6].contents[0]
        counter += 1
        print ("Player rank: {}, Player Name: {}, Position: {}, "
               "Team: {}, TDs: {}").format(counter, name, position, team, tds)
        if counter >= 20:
            break

if __name__ == '__main__':
    main()