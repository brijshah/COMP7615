from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, sys

FONT = 'Arial.ttf'

#rotate
#im = Image.open("abc.jpg")
#im2 = im.rotate(90)
#im2.show()
#im2.save("def.gif")


#mirroring
#img = Image.open("abc.jpg")
#img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
#img_flipped.show()

#Watermark
#in_file(input image)
#text(watermark text to be applied)
#out_file(output image name)
#angle(angle of watermark)
#opacity(default value of opacity)
def add_watermark(in_file, text, out_file='watermark.jpg', angle=23, opacity=0.75):
	#open file and create watermark image of the same size as input image
    img = Image.open(in_file).convert('RGB')
    watermark = Image.new('RGBA', img.size, (0,0,0,0))
    #set a default value of text size, create text, get width and height of text
    size = 2
    n_font = ImageFont.truetype(FONT, size)
    n_width, n_height = n_font.getsize(text)

    #while incrementing font size, search text length that doesnt exceed image dimensions
    while n_width+n_height < watermark.size[0]:
        size += 2
        n_font = ImageFont.truetype(FONT, size)
        n_width, n_height = n_font.getsize(text)
    #obtain proper font size and draw watermark onto center of image
    draw = ImageDraw.Draw(watermark, 'RGBA')
    draw.text(((watermark.size[0] - n_width) / 2,
              (watermark.size[1] - n_height) / 2),
              text, font=n_font)
    #default angle is set at 23, angle is set here using BICUBIC algo
    watermark = watermark.rotate(angle,Image.BICUBIC)
    #using alpha, reduce opacity of watermark(reducing brightness and contrast)
    #default value is .75
    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    #merge watermark image with original and save
    Image.composite(watermark, img, watermark).save(out_file, 'JPEG')
 
if __name__ == '__main__':
	if len(sys.argv) < 3:
	    sys.exit('Usage: %s <input-image> <text> <output-image> ' \
	             '<angle> <opacity> ' % os.path.basename(sys.argv[0]))
	add_watermark(*sys.argv[1:])