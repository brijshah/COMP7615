import sys
import getopt
from PIL import Image
from PIL import ImageOps
from images2gif import writeGif

global manipType
global imagePath
manipType = 0
imagePath = 0

# makes a gif by combining the original image and 7 solarized versions of the
# mage at varrying solarization thresholds and combining them into a single gif
def gif(path):
  # create some more images for some super cool gif business
  im = Image.open(path)
  solarize1 = ImageOps.solarize(im, threshold=32)
  solarize2 = ImageOps.solarize(im, threshold=64)
  solarize3 = ImageOps.solarize(im, threshold=96)
  solarize4 = ImageOps.solarize(im, threshold=128)
  solarize5 = ImageOps.solarize(im, threshold=160)
  solarize6 = ImageOps.solarize(im, threshold=192)
  solarize7 = ImageOps.solarize(im, threshold=224)

  images = [im,
            solarize1,
            solarize2,
            solarize3,
            solarize4,
            solarize5,
            solarize6,
            solarize7,]

  filename = "cool.gif"
  writeGif(filename, images, duration=0.05)

# convert image to greyscale (Luminance mode)
def greyscale(path):
  im = Image.open(path).convert('L')
  im.save('greyscale.jpg')

# invert all colours in an image
# path is absolute path to an image
def invert(path):
  im = Image.open(path)
  inverted = ImageOps.invert(im)
  inverted.save('inverted.jpg')

# inverts all colours in an image via the solarize function
def invertViaSolarize(path):
  im = Image.open(path)
  invertSolarize = ImageOps.solarize(im, threshold=0)
  invertSolarize.save('invertSolarize.jpg')

# pseudo main, handle arg parsing and calling correct image manip function
def main(argv):
  global manipType
  global imagePath
  print argv
  try:
    opts, args = getopt.getopt(argv, "t:p:h",["type=","path=", "help"])
  except getopt.GetoptError:
    sys.exit(2)

  if len(sys.argv) < 2:
    print 'Usage: imageManip.py -t <type> -p <path> or --help'
    sys.exit()

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print 'imageManip.py -t <type> -p <path>'
      print 'Type can be: g (gif), gr (greyscale), i (inverted), or is (invert via solarize)'
      print 'Please provide the absolute path to the image'
      sys.exit()
    elif opt in ("-t", "--type"):
      manipType = arg
    elif opt in ("-p", "--path"):
      imagePath = arg

  if manipType == 'g':
    gif(imagePath)
  elif manipType == 'gr':
    greyscale(imagePath)
  elif manipType == 'i':
    invert(imagePath)
  elif manipType == 'is':
    invertViaSolarize(imagePath)
  else:
     print 'Invalid type, try --help.'

#main method of the program
if __name__ == '__main__':
  main(sys.argv[1:])