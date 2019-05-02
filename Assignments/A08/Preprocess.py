"""
Course: cmps 4883
Assignemt: A08
Date: 5/1/19
Github username: travisbales2304
Repo url: https://github.com/travisbales2304/4883-SWTools-Bales
Name: Travis Bales
Description: 
	pre-proccesses the emoji folder and makes a json file with all the color information needed
    for the main program to create a mosaic
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



#loops through the emoji folder and creates a json file with all the information and saves it
colors = {}
files = glob.glob('Emojis/*.png', recursive=True)
for f in files:
    color_thief = ColorThief(f)
    DC = color_thief.get_color(quality=1)
    jack = f.split("\\")
    colors[jack[1]] = DC
with open('colorinfo.json','w') as f:
    json.dump(colors,f)
