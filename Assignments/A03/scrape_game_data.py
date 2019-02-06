from beautifulscraper import BeautifulScraper
from pprint import pprint
import urllib
from urllib.request import urlretrieve
from time import sleep
import json

scraper = BeautifulScraper()


#opens each file by year with game ids
for x in range(1970,2018):
        f = open("Post %s.txt"%(str(x)),"r")
        for line in f:
                id = line.strip('\n')
                url="http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json" % (id,id)
                urllib.request.urlretrieve(url,'%s.json'%(id))
