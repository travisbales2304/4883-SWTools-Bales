from beautifulscraper import BeautifulScraper
from pprint import pprint
import urllib
import json
import sys
from time import sleep
from random import shuffle

scraper = BeautifulScraper()


for x in range (2009,2019):
    f = open("Reg %s.txt" % str(x),"w")
    for i in range(1,18):

        year = x
        stype = 'REG'
        week = i

        url = "http://www.nfl.com/schedules/%d/%s%s" % (year,stype,str(week))
        page = scraper.go(url)

        divs = page.find_all('div',{"class":"schedules-list-content post expandable primetime type-reg pro-legacy"})
        for div in divs:
            f.write(div['data-gameid'] + '\n')
        divs = page.find_all('div',{"class":"schedules-list-content post expandable type-reg pro-legacy"})
        for div in divs:
            f.write(div['data-gameid'] + '\n')
        divs = page.find_all('div',{"class":"schedules-list-content post type-reg pro-legacy"})
        for div in divs:
            f.write(div['data-gameid'] + '\n')
        sleep(.3)
    f.close()    
for x in range (2018,2019):
    f = open("POST %s.txt" % str(x),"w")

    year = x
    stype = 'POST'

    url = "http://www.nfl.com/schedules/%d/%s" % (year,stype)
    page = scraper.go(url)

    divs = page.find_all('div',{"class":"schedules-list-content"})
    for div in divs:
        f.write(div['data-gameid'] + '\n')
    sleep(.3)
f.close()    
