from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, sys, getopt

FONT = 'Arial.ttf'
global manipType
global imagePath
manipType = 0
imagePath = 0

#rotate
def rotate(path):
    im = Image.open(path)
    im2 = im.rotate(90)
    im2.save('rotate.jpg')

#mirroring
def mirroring(path):
    im = Image.open(path)
    im_flipped = im.transpose(Image.FLIP_LEFT_RIGHT)
    im_flipped.save('mirror.jpg')

#watermark
def add_watermark(path, text, angle=23, opacity=0.75):
    im = Image.open(path).convert('RGB')
    watermark = Image.new('RGBA', im.size, (0,0,0,0))

    size = 5
    font = ImageFont.truetype(FONT, size)
    width, height = font.getsize(text)

    while width + height < watermark.size[0]:
        size += 5
        font = ImageFont.truetype(FONT,size)
        width, height = font.getsize(text)

    draw = ImageDraw.Draw(watermark, 'RGBA')
    draw.text(((watermark.size[0] - width) / 2,
              (watermark.size[1] - height) / 2),
              text, font=font)

    watermark = watermark.rotate(angle, Image.BICUBIC)

    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    Image.composite(watermark, im, watermark).save('watermark.jpg')

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
        elif opt in ("p", "--path"):
            imagePath = arg

    if manipType == 'r':
        rotate(imagePath)
    elif manipType == 'm':
        mirroring(imagePath)
    elif manipType == 'w':
        watermark(imagePath, 'text')
    else:
        print 'Invalid type, try --help.'
 
if __name__ == '__main__':
    main(sys.argv[1:])