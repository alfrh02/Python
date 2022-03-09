#!/usr/bin/env python3
from random import randrange 
from PIL import Image
import fileinput
import os

# the actual algorithm
r = randrange(255) 
g = randrange(255) 
b = randrange(255)

def Rigmarole(r, g, b):
    if (r > 200, g < 200, b < 200): 
            g = g + 30
            b = b + 45
            r = r - 35

    if (r > 200):
        r = 200

    if (g > 235):
        g = 220

    if (b > 235):
        b = 220


    if (r + b + g >= 600):
        r = randrange(125) + 75
        g = randrange(150) + 100
        b = randrange(150) + 100
        if (r < 135, g < 135, b < 135):
            b = b + 100;
        if (r > 200, g < 200, b < 200):
            g = g + 30;
            b = b + 45;
            r = r - 35;

    if (r > b or r > g):
        r = r - 20
        b = b + 20
        g = g + 20

    if (r < 100):
        r = 100;

    if (g < 150):
        g = 150;

    if (b < 135):
        b = 135;

    return r, g, b

#r = Rigmarole(r,g,b)[0]
#g = Rigmarole(r,g,b)[1]
#b = Rigmarole(r,g,b)[2]

print(r)
print(g)
print(b)

currentFolder = os.path.dirname(__file__)
outputFolder = currentFolder + "/output"

if (os.path.exists(outputFolder) == False):
    os.mkdir(outputFolder)

output = outputFolder + "/rgb.png"
outputFile = Image.new("RGB", (64,64), (r,g,b))
outputFile.save(output, "PNG")