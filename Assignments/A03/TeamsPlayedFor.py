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
for x in range(2018,2019):
    f = open("REG %s.txt"%(str(x)),"r")
    for line in f:
        id = line.strip('\n')
        data = openFileJson(id)
        for gameid,gamedata in data.items():
                if gameid != "nextupdate":
                    for driveid,drivedata in gamedata['drives'].items():
                        if driveid != 'crntdrv':
                            for playid,playdata in drivedata['plays'].items():
                                for playerid,player in playdata['players'].items():
                                    for playerinfo in player:
                                     if(not(playerid in playerdata.keys())):
                                           playerdata[playerid] = {}
                                           playerdata[playerid]['Teamsplayedfor'] = []
                                     if(not(playerinfo['clubcode'] in playerdata[playerid]['Teamsplayedfor'])):
                                           playerdata[playerid]['Teamsplayedfor'].append(playerinfo['clubcode'])
f.close()
f = open("Teamdata.json",'w')
f.write(json.dumps(playerdata))
f.close()
pprint(playerdata)
