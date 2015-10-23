#!/usr/bin/python

#-----------------------------------------------------------------------------
#-- SOURCE FILE:    movie.py
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

W, H = 500, 300
DURATION = 2

def makeCircle(t):
    surface = gizeh.Surface(W, H)
    x = W * t / DURATION
    y = H * t / DURATION
    circle = gizeh.circle(30, xy=(x,y), fill=(1,0,0))
    circle.draw(surface)
    return surface.get_npimage()

def makeText(t):
    img = imageio.imread('bg.png')
    W = img.shape[1]
    H = img.shape[0]
    surface = gizeh.Surface.from_image(img)
    x = W * t / DURATION
    y = H * t / DURATION
    text = gizeh.text("H", fontfamily="Helvetica",  fontsize=5, fill=(255,255,255), xy=(x,y))
    text.draw(surface)
    return surface.get_npimage()

def main():
    clip = mpy.VideoClip(makeText, duration=DURATION)
    clip.write_gif("text.gif", fps=30, opt="OptimizePlus", fuzz=10)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Exiting..'