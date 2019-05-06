"""
Course: cmps 4883
Assignemt: A08
Date: 5/1/19
Github username: travisbales2304
Repo url: https://github.com/travisbales2304/4883-SWTools-Bales
Name: Travis Bales

Github username: alejenny97
Repo url:https://github.com/alexjenny97/4883-SWTools-Jenny
Name: Alex Jenny

Description: This program combines a lot functions that we created this semester during projects by combining them together with discord
which allows mulitple people to create works of art and collaborate together.
"""

import discord
from PIL import Image, ImageDraw, ImageFont
import math

client = discord.Client()



'''

These flags that give certain abilities and functionailty
flags:
Requestout: This is a flag to see if someone has made a request to work on the owners picture
Requestinwaiting: This is the id of the person that is waiting to work on a project
Contributors: This is a list of people that have access to working on the project
alwayscheck: This boolean, when true, always displays the picture after an edit.
pictureowner: this is the id of the owner of the picture to edit
pictureinuse: This boolean tells if a picture is currently being edited or not
picturel: This is a list of pictures from the original picture to each edit. This is used for the undo feature and gifify
universalcolor: This is the color used for a lot of the functions
Fontsize: This changes the font size of the text added to a picture
'''
requestout = False
requestinwaiting = ""
contributors = []
alwayscheck = True
pictureowner = ""
pictureinuse = False
picturel = []
universalcolor = (255,255,255)
Fontsize = 10


'''
Funtion name: Tester
Parameters: variable
use: this fuction is used to test new functions about to be added. This makes it easier to test without adding more code at the end for each test
'''
def tester():
    picturel[0].save('Concurrent.gif', format='GIF', append_images=picturel[1:], save_all=True, duration=500, loop=0)
'''
Function name: Gifify
Parameters: integer, This integer represents the milliseconds that each picture will be shown in the gif
use: creates an animated images out of all edited images
'''
def Gifify(time):
    picturel[0].save('Concurrent.gif', format='GIF', append_images=picturel[1:], save_all=True, duration=int(time), loop=0)
'''
Function name: addtext
Parameters: integer,string,integer,integer; First integer being font size, string being the text to add, last two integers being the start x and y coords
use: add text of a certain size and position to a picture
'''
def addtext(fonts,text,x1,y1):
    global pictureinuse
    global universalcolor
    if pictureinuse == False:
        im = Image.open('download.png').convert("RGBA")
        pictureinuse = True
    else:
        im = Image.open('Concurrent.png').convert("RGBA")
    pixels = im.load()
    fontsize = int(fonts)
    w,h = im.size
    size = (w,h)
    newImg = Image.new('RGB', size, (255,255,255))
    drawOnMe = ImageDraw.Draw(newImg)
    for x in range (im.size[0]):
        for y in range(im.size[1]):
            r,g,b,a = pixels[x,y]
            newImg.putpixel((x,y),(r,g,b))
    fnt = ImageFont.truetype('Millo.ttf', fontsize)
    drawOnMe.text((15,15), text, font=fnt, fill=universalcolor)
    updatepicturepos(newImg)
    newImg.save('Concurrent.png','png')
'''
Function name: updatecolor
parameters: integer,integer,integer; each integer represents red,blue,and green values
use: Change the universalcolor to use across multiple functions
'''
def updatecolor(r,g,b):
    global universalcolor
    universalcolor = (int(r),int(g),int(b))
    newImg = Image.new('RGB', (50,50), (int(r),int(g),int(b)))
    newImg.save("Color.png",'png')
'''
Function name: updatepicturepos
Parameters: picture

use: places a picture in the list of pictures that are edited for either undoing or creating a gif
'''
def updatepicturepos(picture):
    picturel.append(picture)
'''
Function name: undo
Parameters: None

use: undo the last change to the picture by removing the last picture in the list of edited pictures
'''
def undo():
    if len(picturel) != 1:
        print(len(picturel))
        picturel.pop()
        picturel[-1].save("Concurrent.png",'png')
'''
Function name: OpenPicture
Parameters: string,string; name being the name of the image, and user being the userid
use: open a new picture for editing as long as the user has permission
'''
def OpenPicture(name, user):
    global pictureinuse
    global pictureowner
    if pictureinuse == False:
        im = Image.open(name + '.png').convert("RGBA")
        pictureinuse = True
        pictureowner = user
    elif pictureowner == user:
        im = Image.open(name + '.png').convert("RGBA")
        pictureinuse = True
    updatepicturepos(im)
    im.save('Concurrent.png','png')
'''
Function name: drawpicture
Parameters: None
use: greyscales the currently in use image
'''
def drawpicture():
    global pictureowner
    global pictureinuse
    if pictureinuse == False:
        im = Image.open('download.png').convert("RGBA")
        pictureinuse = True
    else:
        im = Image.open('Concurrent.png').convert("RGBA")
    w,h = im.size
    size = (w,h)
    newImg = Image.new('RGB', size, (255,255,255))
    pixels = im.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r,g,b,a = pixels[x,y]
            average = int((r + g + b) / 3)
            r = average
            g = average
            b = average
            newImg.putpixel((x,y),(r,g,b))
    updatepicturepos(newImg)
    newImg.save('Concurrent.png','png')
'''
Function name: drawline
Parameters: integer,integer,integer,integer; Integers are x and y coordinates for 2 points that a line is draw between
'''
def drawline(x1,y1,x2,y2):
    global pictureinuse
    if pictureinuse == False:
        im = Image.open('download.png').convert("RGBA")
        pictureinuse = True
    else:
        im = Image.open('Concurrent.png').convert("RGBA")
    global universalcolor
    w,h = im.size
    size = (w,h)
    newImg = Image.new('RGB', size, (255,255,255))
    pixels = im.load()
    for x in range (im.size[0]):
        for y in range(im.size[1]):
            r,g,b,a = pixels[x,y]
            newImg.putpixel((x,y),(r,g,b))
    draw = ImageDraw.Draw(newImg)
    draw.line((int(x1),int(y1),int(x2),int(y2)), fill=universalcolor)
    updatepicturepos(newImg)
    newImg.save('Concurrent.png','png')
'''
Function name: Tint Color
Parameters: color; color being a tuple of 3 integers representing red,blue, and green.
'''
def TintColor(color):
    global pictureinuse
    if pictureinuse == False:
        im = Image.open('download.png').convert("RGBA")
        pictureinuse = True
    else:
        im = Image.open('Concurrent.png').convert("RGBA")
    w,h = im.size
    size = (w,h)
    pixels = im.load()
    newImg = Image.new('RGB',size,(255,255,255))
    for x in range (im.size[0]):
        for y in range(im.size[1]):
            r,g,b,a = pixels[x,y]
            if color == "r":
                if r < 205:
                    newImg.putpixel((x,y),(r + 50,g,b))
                elif r == 255 and g <= 200 and b <= 200:
                    newImg.putpixel((x,y),(255,int(g / 2),int(b / 2)))
                else:
                    newImg.putpixel((x,y),(255,g,b))
            elif color == "g":
                if g < 205:
                    newImg.putpixel((x,y),(r,g + 50,b))
                elif g == 255 and r <= 200 and b <= 200:
                    newImg.putpixel((x,y),(int(r / 2),255,int(b / 2)))
                else:
                    newImg.putpixel((x,y),(r,255,b))
            elif color == "b":
                if b < 205:
                    newImg.putpixel((x,y),(r,g,b + 50))
                elif b == 255 and r <= 200 and g <= 200:
                    newImg.putpixel((x,y),(int(r / 2),int(g / 2),255))
                else:
                    newImg.putpixel((x,y),(r,g,255))


    updatepicturepos(newImg)
    newImg.save('Concurrent.png','png')
'''
Function name: InvertPicture
Parameters: None
use: Inverts a picture by switched the x and y coordinates for each pixel
'''
def InvertPicture():
    global pictureinuse
    if pictureinuse == False:
        im = Image.open('download.png').convert("RGBA")
        pictureinuse = True
    else:
        im = Image.open('Concurrent.png').convert("RGBA")
    w,h = im.size
    size = (h,w)
    pixels = im.load()
    newImg = Image.new('RGB',size,(255,255,255))
    for x in range (im.size[0]):
        for y in range(im.size[1]):
            r,g,b,a = pixels[x,y]
            newImg.putpixel((y,x),(r,g,b))
    updatepicturepos(newImg)
    newImg.save('Concurrent.png','png')
'''
Function name: ResetPicture
Parameters: None
use: Resets the current picture in use to a white picture and releases the owner id for someone else
'''
def ResetPicture():
    global pictureowner
    pictureowner = ""
    global pictureinuse
    pictureinuse = False
    im = Image.open('Concurrent.png').convert("RGBA")
    w,h = im.size
    size = (w,h)
    newImg = Image.new('RGB',size,(255,255,255))
    picturel.clear()
    newImg.save('Concurrent.png','png')
'''
Function name: Authenticate
Parameters: user; the requesting user's id
use: Checks to see if the user has access to editing a picture
'''
def Authenticate(user):
    global pictureowner
    if pictureowner == user:
        return True
    elif pictureowner == "":
        pictureowner = user
        return True
    else:
        for i in contributors:
            if i == user:
                return True
            else:
                return False
'''
Function name: checkowner
Parameters: None
users: checks the owners of the picture's id
'''
def checkowner():
    global pictureowner
    return pictureowner
'''
Function name: Request
Parameters: string; string being the user's id
use: Request's access to edit the owner's picture
'''
def Request(user):
    global requestout
    global requestinwaiting
    requestout = True
    requestinwaiting = user 
'''
Function name: AcceptRequest
Paramteres: None
Uses: accepts a request to edit a picture
'''
def AcceptRequest():

    global requestinwaiting
    global requestout
    if requestinwaiting not in contributors:
        contributors.append(requestinwaiting)
    requestout = False
'''
Function name: AlwaysDisplay
Parameters: None
Use: Toggles displaying the picture after each edit
'''
def AlwaysDisplay():
    global alwayscheck
    if alwayscheck == False:
        alwayscheck = True
    else:
        alwayscheck = False
    #display off or on
'''
Function name: GetAlwaysDisplay
Parameters: None
Use: returns true or false based on the always display boolean
'''
def GetAlwaysDisplay():
    if alwayscheck == True:
        return True
    else:
        return False



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        a = message.content.split(' ')



        if a[-1] == 'gs':
            if Authenticate(message.author.id):
                drawpicture()
                await message.channel.send("Success")
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File('Concurrent.png'))
            else:
                await message.channel.send("You do not have permission to do that.")
        elif a[-1] == 'upload':
            global pictureinuse
            pictureinuse = True
            await message.channel.send("Successfully saved picture")
            await message.attachments[0].save('Concurrent.png')

        elif a[-1] == "ad":
            if Authenticate(message.author.id):
                AlwaysDisplay()
                await message.channel.send("Display toggled")
            else:
                await message.channel.send("You do not have permission to do that.")

        elif a[-1] == "check":
            await message.channel.send(message.author.id)

        elif a[-1] == "ip":
            if Authenticate(message.author.id):
                await message.channel.send("Success")
                InvertPicture()
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File('Concurrent.png'))
            else:
                await message.channel.send("You do not have permission to do that.")

        elif a[-1] == 'rp':
            global pictureowner
            if message.author.id == pictureowner or pictureowner == "":
                ResetPicture()
                await message.channel.send("Picture Reset")
            else:
                await message.channel.send("You do not have permission to do that.")

        elif a[-1] == 'dp':
            await message.channel.send(a[-1], file=discord.File('Concurrent.png'))

        elif a[-1] == "Commands":
            await message.channel.send("```Commands:\n\n gs: Grayscale picture\n\n dl x1 y1 x2 y2: Draw Line on picture\n\n ad: toggle display picture after each change\n\n check: shows user id\n\n ip: invert picture\n\n rp: reset picture\n\n dp: show current picture\n\n req: request editing access from owner\n\n acceptrequest: accept request from last requesting user \n\n co: Check owner id\n\n op x: open picture x\n\n tr x: Tints image to a certain color x; x being r g or b\n\n CC r g b: update color to use in line drawing and text drawing\n\n addtext textsize text xloation ylocation: adds text to location\n\n upload: add attachment with ! upload as description to upload ``` ")

        elif a[-1] == "req":
            global requestout
            if requestout == False:
                Request(message.author.id)
                await message.channel.send("Requested")
            else:
                await message.channel.send("Request already pending")

        elif a[-1] == "acceptrequest":
            if pictureowner == message.author.id:
                await message.channel.send("Accepted")
                AcceptRequest()
            else:
                await message.channel.send("Not owner")


        elif a[-1] == "co":
            await message.channel.send(checkowner())

        elif a[-1] == "undo":
            if Authenticate(message.author.id):
                await message.channel.send("Success")
                undo()
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File('Concurrent.png'))
            else:
                await message.channel.send("You do not have permission to do that")
        elif a[-2] == "op":
            if Authenticate(message.author.id):
                await message.channel.send("Success")
                OpenPicture(a[-1],message.author.id)
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File('Concurrent.png'))
            else:
                await message.channel.send("You do not have permission to do that.")
        elif a[-2] == "gifify":
            if Authenticate(message.author.id):
                await message.channel.send("Success")
                Gifify(a[-1])
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File("Concurrent.gif"))
                else:
                    await message.channel.send("You do not have permission to do that")
        elif a[-2] == 'tr':
            if Authenticate(message.author.id):
                await message.channel.send("Success")
                TintColor(a[-1])
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File('Concurrent.png'))
            else:
                await message.channel.send("You do not have permission to do that")




        elif a[-5] == "addtext":
            if Authenticate(message.author.id):
                await message.channel.send("Success")
                addtext(a[-4],a[-3],a[-2],a[-1])
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File("Concurrent.png"))
            else:
                await message.channel.send("You do not have permission to do that")



        elif a[-5] == 'dl':
            if Authenticate(message.author.id):
                await message.channel.send("Success")
                drawline(a[-4],a[-3],a[-2],a[-1])
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File('Concurrent.png'))
            else:
                await message.channel.send("You do not have permission to do that.")

        elif a[-4] == "cc":
            if Authenticate(message.author.id):
                await message.channel.send("Success")
                updatecolor(a[-3],a[-2],a[-1])
                if GetAlwaysDisplay():
                    await message.channel.send(file=discord.File("Color.png"))
                else:
                    await message.channel.send("You do not have permission to do that")



client.run('NTY4OTk5OTg3NTM5ODY5NzI3.XLqQmA.cOA0QdtyGWsQU7g6ilMY_ySVvUY')
