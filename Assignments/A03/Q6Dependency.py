
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


Team = {}
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
        if(gameid != 'nextupdate'):
            #print(gamedata['home']['abbr'])
            if(not(gamedata['home']['abbr'] in Team.keys())):
                Team[gamedata['home']['abbr']] = 0
            if(not(gamedata['away']['abbr'] in Team.keys())):
                Team[gamedata['away']['abbr']] = 0       
            for driveid,drivedata in gamedata['drives'].items():
                    if driveid != 'crntdrv':
                        for playid,playdata in drivedata['plays'].items():
                            for playerid,player in playdata['players'].items():
                                for playerinfo in player:
                                    if(playerinfo['statId'] == 93):
                                        Team[playerinfo['clubcode']] += 1


Teamname =''
TeamPens = 0
for k,v in Team.items():
    if(int(v) > TeamPens):
        TeamPens = v
        Teamname = k

total = Teamname + ' ' + str(TeamPens)
f.close()
f = open("TeamPens.txt",'w')
f.write(total)
f.close()

