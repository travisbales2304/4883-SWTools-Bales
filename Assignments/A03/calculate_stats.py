"""
Course: cmps 4883
Assignemt: A03
Date: 2/04/19
Github username: TravisBales2304
Repo url: https://github.com/travisbales2304/4883-SWTools-Bales
Name: Travis Bales
Description: Scrape data from the nfl website and store that information into a json file
then we will take the info from the json file and sort through it to get stats for individual
players or teams

"""
import json
import os
import sys
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




##############################################################
# MostTeams()
# This function goes through all the information in the json file
#and finds the person who played for the most teams   
# Returns: 
#    it prints the name and the number of the teams played for
def MostTeams():
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
    print(total + " teams")
##############################################################
# MostTeamsYR()
# This function goes through all the information in the json file
#and finds the person who played for the most teams in a yea
# Returns: 
#    it prints the name and the number of the teams played for in a year
def MostTeamsYR():
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
        print(total + " teams")
##############################################################
# MostYrdsRushedForLoss()
# This function goes through all the information in the json file
#and finds the person who rushed the most yards for a loss
# Returns: 
#    it prints the name and the number of yards they lost
def MostYrdsRushedForLoss():
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
                                            playerdata[playerinfo['playerName']]['YardsRushedforloss'] = 0
                                        if(playerinfo['statId'] == 10 and playerinfo['yards'] < 0):
                                            playerdata[playerinfo['playerName']]['YardsRushedforloss'] += playerinfo['yards']

    mostteams = ''
    numberofmost = 0
    for k,v in playerdata.items():
        for i,x in v.items():
            if(x < numberofmost):
                mostteams = k
                numberofmost = x
    total = mostteams + " " + str(numberofmost)
    print(total + " Yards Rushed for loss")
##############################################################
# MostRushesForLoss()
# This function goes through all the information in the json file
#and finds the person who lost yards the most amount of times with a rush
# Returns: 
#    it prints the name and the number times they rushed for a loss
def MostRushesForLoss():
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
                                            playerdata[playerinfo['playerName']]['YardsRushedforloss'] = 0
                                        if(playerinfo['statId'] == 10 and playerinfo['yards'] < 0):
                                            playerdata[playerinfo['playerName']]['YardsRushedforloss'] += 1

    mostteams = 'g'
    numberofmost = 0
    for k,v in playerdata.items():
        for i,x in v.items():
            if(x > numberofmost):
                mostteams = k
                numberofmost = x
    total = mostteams + " " + str(numberofmost)
    print(total +" Times rushed for a loss")
##############################################################
# MostPassesForLoss()
# This function goes through all the information in the json file
#and finds the person who threw the ball the most times for a loss of yardage
# Returns: 
#    it prints the name and the number of passes that lost yards
def MostPassesForLoss():
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
                                            playerdata[playerinfo['playerName']]['YardsRushedforloss'] = 0
                                        if(playerinfo['statId'] == 20):
                                            playerdata[playerinfo['playerName']]['YardsRushedforloss'] += 1

    mostteams = 'g'
    numberofmost = 0
    for k,v in playerdata.items():
        for i,x in v.items():
            if(x > numberofmost):
                mostteams = k
                numberofmost = x
    total = mostteams + " " + str(numberofmost)
    print(total +" Times passed for a loss")
##############################################################
# TeamMostPenalties()
# This function goes through all the information in the json file
#and finds the team that had the most penalties
# Returns: 
#    it prints the name of the team and the number of penalties they got
def TeamMostPenalties():
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
    print(total + " penalties")
##############################################################
# TeamMostYrdsPenalties()
# This function goes through all the information in the json file
#and finds the team that lost the most yards in penalties
# Returns: 
#    it prints the name of the team and the number of yards lost
def TeamMostYrdsPenalties():
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
                                            if(int(playerinfo['yards']) !=None):
                                                Team[playerinfo['clubcode']] += playerinfo['yards']


    Teamname =''
    TeamPens = 0
    for k,v in Team.items():
        if(v > TeamPens):
            TeamPens = v
            Teamname = k

    total = Teamname + ' ' + str(TeamPens)
    print(total + " Yards lost in penalties")
##############################################################
# AvgPlaysPerGame()
# This function goes through all the information in the json file
# and calculates the average plays per game
# Returns: 
#    it prints the number of plays per game divided by the amount of games
def AvgPlaysPerGame():
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
    print(str(total) + " Average plays a game")
##############################################################
# LongestFG()
# This function goes through all the information in the json file
#and finds the person with the longest fieldgoal
# Returns: 
#    it prints the name of the player and the fieldgoal in yards
def LongestFG():
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
                                        if(playerinfo['statId'] == 88 or playerinfo['statId'] == 71 or playerinfo['statId'] == 70 or playerinfo['statId'] == 69):
                                            if(not(playerinfo['playerName'] in FGdata.keys())):
                                                FGdata[playerinfo['playerName']] = {}
                                                FGdata[playerinfo['playerName']]['FGPR'] = 0
                                                if(playerinfo['statId'] == 70):
                                                    if(int(playerinfo['yards']) > FGdata[playerinfo['playerName']]['FGPR']):
                                                        FGdata[playerinfo['playerName']]['FGPR'] = int(playerinfo['yards'])


    name = ''
    FieldGoalPersonalRecord = 0
    for k,v in FGdata.items():
        for i,x in v.items():
            if(x > FieldGoalPersonalRecord):
                name = k
                FieldGoalPersonalRecord = x
    total = name + ' ' + str(FieldGoalPersonalRecord) 
    print(total + " Yard Field goal Personal Best")
##############################################################
# MostFG()
# This function goes through all the information in the json file
#and finds the person who made the most field goals
# Returns: 
#    it prints the name of the person and the number of fieldgoals made
def MostFG():
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
                                        if(playerinfo['statId'] == 88 or playerinfo['statId'] == 71 or playerinfo['statId'] == 70 or playerinfo['statId'] == 69):
                                            if(not(playerinfo['playerName'] in FGdata.keys())):
                                                FGdata[playerinfo['playerName']] = {}
                                                FGdata[playerinfo['playerName']]['FG'] = 1
                                            else:
                                                FGdata[playerinfo['playerName']]['FG'] += 1
    name = ''
    FieldGoals = 0
    for k,v in FGdata.items():
        for i,x in v.items():
            if(x > FieldGoals):
                name = k
                FieldGoals = x
    total = name + ' ' + str(FieldGoals) 
    print(total + " Field Goals made")
##############################################################
# MostFailedFG()
# This function goes through all the information in the json file
#and finds the person that failed the most fieldgoalds
# Returns: 
#    it prints the name of the person and the number of failed field goalds
def MostFailedFG():
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
                                        if(playerinfo['statId'] == 88 or playerinfo['statId'] == 71 or playerinfo['statId'] == 69):
                                            if(not(playerinfo['playerName'] in FGdata.keys())):
                                                FGdata[playerinfo['playerName']] = {}
                                                FGdata[playerinfo['playerName']]['FGF'] = 1
                                            else:
                                                FGdata[playerinfo['playerName']]['FGF'] += 1
    name = ''
    FieldGoalF = 0
    for k,v in FGdata.items():
        for i,x in v.items():
            if(x > FieldGoalF):
                name = k
                FieldGoalF = x
    total = name + ' ' + str(FieldGoalF) 
    print(total + " Field Goals missed")
##############################################################
# MostDroppedPasses()
# This function goes through all the information in the json file
#and finds the person who threw the most passes that were failed
# Returns: 
#    it prints the name of the player and the number of failed passes
def MostDroppedPasses():
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
    print(total + " Passes dropped by receiver")




print('Name: Travis Bales \nAssignment: A03 - Nfl Stats \nDate: 2/12/2019\n\n')

print('Find the player(s) that played for the most teams.\nAnswer:\n')
#anser to question
MostTeams() 

print('\n\n')

print('Find the player(s) that played for multiple teams in one year.\nAnswer:\n')
#anser to question
MostTeamsYR()

print('\n\n')

print('Find the player(s) that had the most yards rushed for a loss.\nAnswer:\n')
#anser to question
MostYrdsRushedForLoss()

print('\n\n')

print('Find the player(s) that had the most rushes for a loss.\nAnswer:\n')
#anser to question
MostRushesForLoss()

print('\n\n')

print('Find the player(s) with the most number of passes for a loss.\nAnswer:\n')
#anser to question
MostPassesForLoss()

print('\n\n')

print('Find the team with the most penalties.\nAnswer:\n')
#anser to question
TeamMostPenalties()

print('\n\n')

print('Find the team with the most yards in penalties.\nAnswer:\n')
#anser to question
TeamMostYrdsPenalties()

print('\n\n')

print('Average number of plays in a game.\nAnswer:\n')
#anser to question
AvgPlaysPerGame()


print('\n\n')

print('Longest field goal.\nAnswer:\n')
#anser to question
LongestFG()


print('\n\n')

print('Most field goals.\nAnswer:\n')
#anser to question
MostFG()


print('\n\n')

print('Most missed field goals.\nAnswer:\n')
#anser to question
MostFailedFG()
print('\n\n')

print('Most dropped passes\nAnswer:\n')
#anser to question
MostDroppedPasses()
print('\n\n')
