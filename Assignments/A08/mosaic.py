"""
Course: cmps 4883
Assignemt: A08
Date: 5/1/19
Github username: travisbales2304
Repo url: https://github.com/travisbales2304/4883-SWTools-Bales
Name: Travis Bales
Description: 
	Start with an image, loop through that image and replace every pixel with an emoji. Each emoji
    replacement will be chosen based on it's dominant color and how close it is to the original pictures
    pixel color.
"""


from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image
import sys,os
import pprint
import requests
from math import sqrt
import glob
import argparse
from colorthief import ColorThief
import json

'''
Resizes pictures to a square given a specific length
'''
def resize(img,width):
    """
    This resizes the img while maintining aspect ratio. Keep in 
    mind that not all images scale to ascii perfectly because of the
    large discrepancy between line height line width (characters are 
    closer together horizontally then vertically)
    """
    wpercent = float(width / float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width ,hsize), Image.ANTIALIAS)
    return img

'''
This fuction takes a red, blue, and green value as well as it's x and y coordinates and finds
the closest emoji to that color combination and replaces it on a newly created picture to form an
emoji mosaic
'''
def getclosest(red,green,blue,x,y,w,h):
    closestemoji = ""
    closestdistance = 10000
    with open('colorinfo.json','r') as f:
        colorlist = json.load(f)
        for k,v in colorlist.items():
            name  = k
            r = v[0]
            g = v[1]
            b = v[2]
            d = sqrt(pow(red - r,2) + pow(green - g,2) + pow(blue - b,2))
            if d < closestdistance:
                closestdistance = d
                closestemoji = name
    im = Image.open('Emojis/' + closestemoji).convert("RGBA")
    im = resize(im,w)
    newImg.paste(im,(x*w,y*h),im)



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True,
	help="folder of images to create mosaic with")
ap.add_argument("-r","--size", required=True,
    help="size of emojis to create picture with")
ap.add_argument('-p','--sizeoforiginal', required=True,
    help="size of original picture to create mosaic with")
ap.add_argument("-s", "--image", required=True,
	help="image to create a mosaic out of")
args = vars(ap.parse_args())
path = args["folder"] + "/"





#import starting picture
im = Image.open(args['image'])
im = resize(im,int(args['sizeoforiginal']))
im.show()
pixels = im.load()
w,h = im.size


#create new image that is (width of emoji) X (height of emoji) in size
    #store in folder called "Mosaic images"
picturew = int(args["size"])
pictureh = int(args["size"])
size = (w*picturew,h*pictureh)
newImg = Image.new('RGB', size, (255,255,255))
pixels2 = newImg.load()


#get set of color values from the original picture

#loop through the color values
    #locate emoji that closely matches that color
        #place that emoji in that place
for x in range(im.size[0]):
    for y in range(im.size[1]):
        r,g,b = pixels[x,y]
        getclosest(r,g,b,x,y,picturew,pictureh)


name = args['image'].split('.')
name = name[0]
newImg.show()
newImg.save(name + '_mosaic.png','png')
exit()
