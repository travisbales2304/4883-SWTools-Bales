
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


list1 = []
for x in range(2009,2019):
    f = open("REG %s.txt"%(str(x)),"r")
    for line in f:
        id = line.strip('\n')
        list1.append(id)
    f.close()


drivenumber = 0
for x in range(0,len(list1)):
    data = openFileJson(list1[x])
    for gameid,gamedata in data.items():
        if(gameid != 'nextupdate'):    
            for driveid,drivedata in gamedata['drives'].items():
                if driveid != 'crntdrv':
                    for playid,playdata in drivedata['plays'].items():
                        drivenumber += 1



total = drivenumber // len(list1)
f.close()
f = open("AvgDrives.txt",'w')
f.write(str(total))
f.close()
