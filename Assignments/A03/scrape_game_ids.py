from beautifulscraper import BeautifulScraper
from pprint import pprint
import urllib
import json
import sys
from time import sleep
from random import shuffle

scraper = BeautifulScraper()


for x in range (1970,2019):
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
    f = open("Post %s.txt" % str(x),'w')
    url = "http://www.nfl.com/schedules/%d/POST" % (year)
    page = scraper.go(url)
    divs = page.find_all('div',{"class":"schedules-list-content post expandable primetime type-wc pro-legacy"})
    for div in divs:
        f.write(div['data-gameid'] + '\n')
    divs = page.find_all('div',{"class":"schedules-list-content post expandable  type-wc pro-legacy"})
    for div in divs:
        f.write(div['data-gameid'] + '\n')
    divs = page.find_all('div',{"class":"schedules-list-content post expandable primetime type-div pro-legacy"})
    for div in divs:
        f.write(div['data-gameid'] + '\n')
    divs = page.find_all('div',{"class":"schedules-list-content post expandable  type-div pro-legacy"})
    for div in divs:
        f.write(div['data-gameid'] + '\n')
    divs = page.find_all('div',{"class":"schedules-list-content post expandable  type-con pro-legacy"})
    for div in divs:
        f.write(div['data-gameid'] + '\n')
    divs = page.find_all('div',{"class":"schedules-list-content post expandable primetime type-pro pro-legacy"})
    for div in divs:
        f.write(div['data-gameid'] + '\n')
    divs = page.find_all('div',{"class":"schedules-list-content post expandable primetime type-sb pro-legacy"})
    for div in divs:
        f.write(div['data-gameid'] + '\n')
    f.close()


