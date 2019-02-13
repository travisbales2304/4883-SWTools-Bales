
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


FGdata = {}
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
                #print(gameid)
                # go straight for the drives
                for driveid,drivedata in gamedata['drives'].items():
                    if driveid != 'crntdrv':
                        for playid,playdata in drivedata['plays'].items():
                            for playerid,player in playdata['players'].items():
                                for playerinfo in player:
                                    if(playerinfo['statId'] == 14):
                                        if(not(playerinfo['playerName'] in FGdata.keys())):
                                            FGdata[playerinfo['playerName']] = {}
                                            FGdata[playerinfo['playerName']]['FailedPasses'] = 1
                                        else:
                                            FGdata[playerinfo['playerName']]['FailedPasses'] += 1
name = ''
FailedPass = 0
for k,v in FGdata.items():
    for i,x in v.items():
        if(x > FailedPass):
            name = k
            FailedPass = x
total = name + ' ' + str(FailedPass) 
print(total)
f.close()
f = open("FP.txt",'w')
f.write(total)
f.close()


