import gizeh
import moviepy.editor as mpy 
from random import randint
import imageio

W, H = 500, 300
DURATION = 2

def makeCircle(t):
    surface = gizeh.Surface(W, H)
    x = W * t / DURATION
    y = H * t / DURATION
    circle = gizeh.circle(30, xy=(x,y), fill=(1,0,0))
    circle.draw(surface)
    return surface.get_npimage()

#works on linux, not on mac, fuck
def makeText(t):
    img = imageio.imread('tiger.png')
    W = img.shape[1]
    H = img.shape[0]
    surface = gizeh.Surface.from_image(img)
    #surface = gizeh.Surface(W, H)
    x = W * t / DURATION
    y = H * t / DURATION
    text = gizeh.text("H", fontfamily="Helvetica",  fontsize=5,
                  fill=(255,255,255), xy=(x,y))
    text.draw(surface)
    return surface.get_npimage()

def main():
    clip = mpy.VideoClip(makeText, duration=DURATION)
    clip.write_gif("text.gif", fps=30, opt="OptimizePlus", fuzz=10)

if __name__ == '__main__':
    main()
