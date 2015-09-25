from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, sys, getopt

#Globals
FONT = 'Arial.ttf'
global manipType
global imagePath
global blueBackground
manipType = 0
imagePath = 0
blueBackground = (3, 52, 103)

#rotate
#loads an image with a user given path and returns a copy of
#the image rotated the given number of degrees counter clckwise around
#its centre.
def rotate(path):
    im = Image.open(path)
    im2 = im.rotate(90)
    im2.save('rotate.jpg')

#mirroring
#loads an image with a user given path and returns a copy of
#the image flipped or rotated.
def mirroring(path):
    im = Image.open(path)
    im_flipped = im.transpose(Image.FLIP_LEFT_RIGHT)
    im_flipped.save('mirror.jpg')

#watermark
#loads a user given path, and adds a watermark layer on top
#of a copy of the image using system font.
def add_watermark(path, text, angle=23, opacity=0.75):
	#open the input file and create watermark image of similar dimensions
    im = Image.open(path).convert('RGB')
    watermark = Image.new('RGBA', im.size, (0,0,0,0))

    #initialize size of font and create text by obtaining height and width
    size = 5
    font = ImageFont.truetype(FONT, size)
    width, height = font.getsize(text)

    #by incrementing font size, we search for text that wont exceed image size
    while width + height < watermark.size[0]:
        size += 5
        font = ImageFont.truetype(FONT,size)
        width, height = font.getsize(text)

    #obtain correct font size and draw text onto center of watermark image
    draw = ImageDraw.Draw(watermark, 'RGBA')
    draw.text(((watermark.size[0] - width) / 2,
              (watermark.size[1] - height) / 2),
              text, font=font)

    #rotate image by default angle, using BICUBIC algorithm
    watermark = watermark.rotate(angle, Image.BICUBIC)

    #alpha channel used to reduce opacity of watermark(reducing brightness
    #and contrast) by default value of 0.25
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    #merge watermark image back into original image and save
    Image.composite(watermark, im, watermark).save('watermark.jpg')

# checks to see if two colours are similar to eachother by adding the difference
# between all the RGB values, used for reverseChromaKey
def matchColours(pixelColour, matchToColour):
  if (abs(pixelColour[0] - matchToColour[0]) +
      abs(pixelColour[1] - matchToColour[1]) +
      abs(pixelColour[0] - matchToColour[0]) < 36):
    return True


# like chroma key, except we're keeping the same background and modifying all
# the other colours, we're going to use this to create the nyancat gif where
# only the cat and rainbow change colours
def reverseChromaKey(image):
  global blueBackground
  global white
  global black

  baseImage = Image.open(image)
  pixels = list(baseImage.getdata())

  # loop through all pixels
  count = 0
  for pixel in pixels:
    # check if the pixel is a background pixel
    if matchColours(pixel, blueBackground):
      count = count + 1
      continue
    else:
      # invert
      pixels[count] = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
      count = count + 1

  # end of loop, write the new pixel data to the image
  newImage = Image.new('RGB', (baseImage.size[0], baseImage.size[1]), (255, 255, 255))
  newImage.putdata(pixels)
  newImage.save('reverseChromaKey.jpg')

def main(argv):
    global manipType
    global imagePath
    print argv

    try:
        opts, args = getopt.getopt(argv, "t:p:h", ["type=", "path=", "help"])
    except getopt.GetoptError:
        sys.exit(2)

    if len(sys.argv) < 2:
        print 'Usage: a2.py -t <type> -p <path> or --help'
        sys.exit()

    for opt, arg in opts:
        if opt in ("h", "--help"):
            print 'a2.py -t <type> -p <path>'
            print 'Type can be r (rotate), m (mirroring), w (watermark) or c (chroma)'
            print 'Please provide the absolute path to image'
            sys.exit()
        elif opt in ("-t", "--type"):
            manipType = arg
        elif opt in ("-p", "--path"):
            imagePath = arg

    if manipType == 'r':
        rotate(imagePath)
    elif manipType == 'm':
        mirroring(imagePath)
    elif manipType == 'w':
        add_watermark(imagePath, 'text')
    elif manipType == 'c':
        reverseChromaKey(imagePath)
    else:
        print 'Invalid type, try --help.'

if __name__ == '__main__':
    main(sys.argv[1:])