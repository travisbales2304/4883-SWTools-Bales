
import json
import sys
import os
from pprint import pprint


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
def openFileJson(file):
    try:
      f = open('%s.json' % (str(file)),'r')
      data = f.read()
      if is_json(data):
          return json.loads(data)
      else:
          print("Error: Not json.")
          return {}
    except IOError:
        print("Error: Game file doesn't exist.")
        return {}
playerdata = {}
list1 = []
for x in range(2009,2019):
    f = open("REG %s.txt"%(str(x)),"r")
    for line in f:
        id = line.strip('\n')
        list1.append(id)
    f.close()
for x in range(0,len(list1)):
    data = openFileJson(list1[x])
    for gameid,gamedata in data.items():
            if gameid != "nextupdate":
                for driveid,drivedata in gamedata['drives'].items():
                    if driveid != 'crntdrv':
                        for playid,playdata in drivedata['plays'].items():
                            for playerid,player in playdata['players'].items():
                                for playerinfo in player:
                                    if(not(playerinfo['playerName'] in playerdata.keys())):
                                        playerdata[playerinfo['playerName']] = {}
                                        playerdata[playerinfo['playerName']]['Teamsplayedfor'] = []
                                    if(not(playerinfo['clubcode'] in playerdata[playerinfo['playerName']]['Teamsplayedfor'])):
                                        playerdata[playerinfo['playerName']]['Teamsplayedfor'].append(playerinfo['clubcode'])

mostteams = ''
numberofmost = 0
for k,v in playerdata.items():
    for i,x in v.items():
            if(len(x) > numberofmost and len(x) != 32):
                numberofmost = len(x)
                mostteams = k

total = mostteams + " " + str(numberofmost)
print(total)
#print(mostteams,numberofmost)
f.close()
f = open("Teamdata.txt",'w')
f.write(total)
f.close()
#pprint(playerdata)
