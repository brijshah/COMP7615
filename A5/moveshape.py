#!/usr/bin/python

#-----------------------------------------------------------------------------
#-- SOURCE FILE:    moveshape.py
#--
#-- FUNCTIONS:      makeCircle(t)
#--                 makeText(t)
#--                 main()
#--
#-- DATE:           October 23, 2015
#--
#-- DESIGNERS:      Brij Shah & Callum Styan
#--
#-- PROGRAMMERS:    Brij Shah & Callum Styan
#-----------------------------------------------------------------------------

import gizeh, imageio, argparse
import moviepy.editor as mpy

parser = argparse.ArgumentParser(description='Move Shape')
parser.add_argument('-c', '--colour', dest='colour', help='colour of shape', required=True)
parser.add_argument('-s', '--size', dest='radius', help='size of shape(in radians)', required=True)
args = parser.parse_args()

#Global Variables
W, H = 500, 300
DURATION = 2

# Converts string into an RGB tuple to pass into the make Circle method
def stringToRGB(string):
    colour = ()
    if string == 'red':
        colour = (1,0,0)
    if string == 'green':
        colour = (0,1,0)
    if string == 'blue':
        colour = (0,0,1)
    return colour

# Creates a black canvas, a circle with given specifications and moves the shape in a diagonal line.
# 't' is a frame
def makeCircle(t):
    fill = stringToRGB(args.colour)
    surface = gizeh.Surface(W, H)
    x = W * t / DURATION
    y = H * t / DURATION
    circle = gizeh.circle(int(args.radius), xy=(x,y), fill=fill)
    circle.draw(surface)
    return surface.get_npimage()

# Pseudomain method
# Saves makeCircle frames as .gif video
def main():
    clip = mpy.VideoClip(makeCircle, duration=DURATION)
    clip.write_gif("shape.gif", fps=30, opt="OptimizePlus", fuzz=10)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Exiting..'