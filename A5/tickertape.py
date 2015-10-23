#!/usr/bin/python

#-----------------------------------------------------------------------------
#-- SOURCE FILE:    tickertape.py
#--
#-- FUNCTIONS:      makeText(t)
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

parser = argparse.ArgumentParser(description='Text Ticker Tape')
parser.add_argument('-t', '--text', dest='text', help='text to animate', required=True)
parser.add_argument('-b', '--background', dest='background', help='background image', required=True)
args = parser.parse_args()

DURATION = 2

def makeText(t):
    img = imageio.imread(args.background)
    W = img.shape[1]
    H = img.shape[0]
    surface = gizeh.Surface.from_image(img)
    x = W * t / DURATION
    y = H * t / DURATION
    text = gizeh.text(args.text, fontfamily="Helvetica",  fontsize=5, fill=(255,255,255), xy=(x,y))
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