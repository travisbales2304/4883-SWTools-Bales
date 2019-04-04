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

def brightness(r,g,b):
    """A function to return the calculated "brightness" of a color.
    http://www.nbdtech.com/Blog/archive/2008/04/27/Calculating-the-Perceived-Brightness-of-a-Color.aspx
    Arguments:
        r: [int]
        g: [int]
        b: [int]
    Returns:
        Values between 0-1 (percent of 0-255)
    Used By:
        get_dominant_colors
    """
    return sqrt(pow(r,2) * .241  + pow(g,2) * .691 + pow(b,2) * .068 ) / 255

def find_histogram(clt):
    """ Create a histogram with k clusters
    Arguments:
        :param: clt
        :return:hist
    Used By:
        get_dominant_colors
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist


def get_color_data(r,g,b,d=3):
    """Get color name and hsv from color api.

    Arguments:
        r -- red   [int]
        g -- green [int]
        b -- blue  [int]
    Returns:
        json
    """
    payload = {'r':r, 'g':g, 'b':b,'d':d}
    r = requests.get('http://cs.mwsu.edu/~griffin/color-api/', params=payload)
    return r.json()


def extract_cluster_color_values(hist, centroids,ignore_background=False):
    """Get the dominant colors of an image.

    Arguments:
        hist        -- [numpy.ndarray]
        centroids   -- [numpy.ndarray] 
    Returns:
        dictionary of color values
    Used By:
        get_dominant_colors
    """

    colors = []
    
    for (percent, color) in zip(hist, centroids):
        rgb = []
        total = 0
        for c in color:
            c = round(float(c))
            total += c
            rgb.append(c)
        if ignore_background:
            if total > 15 and total < 750:
                colors.append({'percent':round(float(percent),2),'rgb':rgb})
        else:
            colors.append({'percent':round(float(percent),2),'rgb':rgb})

    return colors

def plot_colors(hist, centroids):
    """Get the dominant colors of an image.

    Arguments:
        hist        -- [numpy.ndarray]
        centroids   -- [numpy.ndarray] 
    Returns:
        plot image
    """
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


def get_dominant_colors(img,save_path=None,n=3):
    """Get the dominant colors of an image.

    Arguments:
        img         -- the image [string, numpy.ndarray]
        save_path   -- out path for saving [string] (default None)
        n           -- number of clusters [int] (default 3)
    Returns:
        dictionary of colors
        load_subimages_data
    Requres:
        extract_cluster_color_values
        query_color
        brightness
    """

    #bg,_ = determine_background(img_path)

    # if its string open it
    if isinstance(img,str):
        if os.path.isfile(img):
            img = cv2.imread(img)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            print("Error: image path not valid")

    img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number

    clt = KMeans(n_clusters=n) #cluster number
    clt.fit(img)

    hist = find_histogram(clt)
    colors = extract_cluster_color_values(hist, clt.cluster_centers_)

    if save_path != None:
        bar = plot_colors(hist, clt.cluster_centers_)
        cv2.imwrite(save_path,bar)
        # plt.axis("off")
        # plt.imshow(bar)
        # plt.show()

    start_delta = 3

    # loop through each cluster
    for i in range(len(colors)):
        c = []
        d = start_delta
        # while we haven't found a named color match (increment delta)
        while len(c) < 1:
            #c = query_color(colors[i]['rgb'][0],colors[i]['rgb'][1],colors[i]['rgb'][2],d)
            c = get_color_data(colors[i]['rgb'][0],colors[i]['rgb'][1],colors[i]['rgb'][2],d)
            d += 3
        colors[i]['named_data'] = c
        colors[i]['brightness'] = brightness(colors[i]['rgb'][0],colors[i]['rgb'][1],colors[i]['rgb'][2])

    return colors













'''
#outputs as BLUE,GREEN,RED
Picture_values = []
Picture_name = []

files = glob.glob('*.jpg', recursive=True)
for f in files:
    tmp = f
    colors1 = get_dominant_colors(tmp,'output.jpg',1)
    a = str(colors1[0]['rgb'])
    a.strip("[]")
    Picture_values.append(a)
    Picture_name.append(f)
print(Picture_values)
print(Picture_name)
'''





def getclosest(red,green,blue,x,y,w,h):
        print(x)
        files = glob.glob('*.jpg', recursive=True)
        for f in files:
            tmp = Image.open(f).convert("RGBA")
            tmp = resize(tmp,10)
            newImg.paste(tmp,(x*w,y*h),tmp)


       



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True,
	help="folder of images to compar")
ap.add_argument("-s", "--image", required=True,
	help="image to compare")
args = vars(ap.parse_args())


path = args["folder"] + "/"



#Check for processed images


#import starting picture
im = Image.open(args['image'])
im.show()
pixels = im.load()
w,h = im.size


#Create new image to paste smaller images
picturew = 10
pictureh = 10
size = (w*picturew,h*pictureh)
newImg = Image.new('RGB', size, (255,255,255))
pixels2 = newImg.load()


#Go through start image and paste smaller image
for x in range(im.size[0]):
    for y in range(im.size[1]):
        r,g,b = pixels[x,y]
        getclosest(r,g,b,x,y,picturew,pictureh)

        




newImg.show()

