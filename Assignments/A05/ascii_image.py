"""
Course: cmps 4883
Assignemt: A03
Date: 2/04/19
Github username: travisbales2304
Repo url: https://github.com/travisbales2304/4883-SWTools-Bales
Name: Travis Bales
Description: 
    Take a picture convert it to grayscale and then apply letters from a certain
    front as representations of each section of the picture.

"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter



"""
Function name: img_to_ascii
Args: path name, output name, font, fontsize
this function will take a specified image and
convert it into a text art image 
"""
def img_to_ascii(**kwargs):
    """ 
    The ascii character set we use to replace pixels. 
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-2
    """
    ascii_chars = [ 'A', 'B', 'L', 'i', 'H', 'v', 'G', 'h', 'o', 'l', 'W']

    path = kwargs.get('path',None)
    font=kwargs.get('font',None)
    fontsize=int(kwargs.get('fontsize',None))
    outputname = kwargs.get('output',None)

    #in case you want the default font
    if(font != None):
        font='Millo.ttf'
    im = Image.open(path)
    im = resize(im,200)
    w,h = im.size
    size = (w*fontsize,h*fontsize)
    imlist=list(im.getdata())
    fnt = ImageFont.truetype(font, 24)
    newImg = Image.new('RGB', size, (255,255,255))
    drawOnMe = ImageDraw.Draw(newImg)
    i=0
    for x in range(h):
        for y in range(w):
            #gets the rbg of each pixel and saves in order to a list
            r,g,b = imlist[i]
            #converts the rbg value to grayscale
            gray = int((r + b + g) / 3)
            #gets the character to use for the position
            char = ascii_chars[gray // 25]
            #draws each letter to the screen with the saved rgb value
            drawOnMe.text((y*fontsize,x*fontsize), char, font=fnt, fill=(r,g,b))
            #increment the list
            i+=1
    """
    i = 1
    for val in imlist:
        ch = ascii_chars[val // 25].decode('utf-8')
        sys.stdout.write()
        i += 1
        if i % width == 0:
            sys.stdout.write("\n")
    """
    newImg.show()
    newImg.save(outputname+'.jpg')

    

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


if __name__=='__main__':
    path =sys.argv[1]
    output=sys.argv[2]
    font=sys.argv[3]
    fontsize=sys.argv[4]
    img_to_ascii(path=path,output=output,font=font,fontsize=fontsize)


    
