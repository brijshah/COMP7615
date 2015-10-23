import gizeh as gz
import moviepy.editor as mpy
from random import randint

ballRadius = 25
screenWidth, screenHeight = 300,300
circleCoordinates = (25, 25)
circleCoordinates1 = (275,275)
DURATION = 30

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


def makeFrame(t):
    global circleCoordinates, circleCoordinates1
    surface = gz.Surface(screenWidth, screenHeight)

    circleCoordinates = edgeDetection(circleCoordinates)
    circleCoordinates1 = edgeDetection(circleCoordinates1)

    bCircle = gz.circle(ballRadius, xy=circleCoordinates, fill=(1,0,0))
    circle1 = gz.circle(ballRadius, xy=circleCoordinates1, fill=(0,0,1))

    bCircle.draw(surface)
    circle1.draw(surface)
    return surface.get_npimage()

def main():
    clip = mpy.VideoClip(makeFrame, duration=DURATION)
    clip.write_gif("rand.gif", fps=60, opt="OptimizePlus", fuzz=10)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Exiting..'