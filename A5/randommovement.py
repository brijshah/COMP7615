#!/usr/bin/python

#-----------------------------------------------------------------------------
#-- SOURCE FILE:    randommovement.py
#--
#-- FUNCTIONS:      edgeDetection(coordinates)
#--                 makeFrame(t)
#--                 main()
#--
#-- DATE:           October 23, 2015
#--
#-- DESIGNERS:      Brij Shah & Callum Styan
#--
#-- PROGRAMMERS:    Brij Shah & Callum Styan
#-----------------------------------------------------------------------------

import gizeh as gz
import moviepy.editor as mpy
from random import randint
import argparse

# argument parser for command line arguments
parser = argparse.ArgumentParser(description='Random Movement')
parser.add_argument('-r', '--radius', dest='radius', help='size of ball(in radians)', required=True)
parser.add_argument('-w', '--width', dest='width', help='width of canvas', required=True)
parser.add_argument('-ht', '--height', dest='height', help='height of canvas', required=True)
args = parser.parse_args()

# global variables
ballRadius = int(args.radius)
screenWidth, screenHeight = int(args.width), int(args.height)
circleCoordinates = (25, 25)
circleCoordinates1 = (275,275)
DURATION = 30

# detects edges when shapes are in proximity of cavas edge
def edgeDetection(coordinates):
    x = coordinates[0] + randint(-5,5)
    y = coordinates[1] + randint(-5,5)
    if x + ballRadius > screenWidth:
        x = screenWidth - ballRadius
    elif x - ballRadius < 0:
        x = ballRadius

    if y + ballRadius > screenHeight:
        y = screenHeight - ballRadius
    elif y - ballRadius < 0:
        y = ballRadius
    return (x,y)

# creates a a black canvas, two shapes and animates them with edge detection
# t is a frame
def makeMovement(t):
    global circleCoordinates, circleCoordinates1
    surface = gz.Surface(screenWidth, screenHeight)

    circleCoordinates = edgeDetection(circleCoordinates)
    circleCoordinates1 = edgeDetection(circleCoordinates1)

    bCircle = gz.circle(ballRadius, xy=circleCoordinates, fill=(1,0,0))
    circle1 = gz.circle(ballRadius, xy=circleCoordinates1, fill=(0,0,1))

    bCircle.draw(surface)
    circle1.draw(surface)
    return surface.get_npimage()

# Pseudomain
def main():
    clip = mpy.VideoClip(makeMovement, duration=DURATION)
    clip.write_gif("rand.gif", fps=60, opt="OptimizePlus", fuzz=10)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Exiting..'