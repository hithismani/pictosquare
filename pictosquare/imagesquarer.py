from PIL import Image, ImageOps
import os
import re
from colorthief import ColorThief

def imageSquare(img_path, filename, watermark, position, watermark_size, color):
    im_pth = img_path+"/"+filename
    desired_size = 800  # Default Size
    minimum_size = 800
    file_name, file_extension = os.path.splitext(filename)

    im = Image.open(im_pth)

    x, y = im.size

    if x > y:  # Set Max Image Dimension
        desired_size = x
        minimum_size = y
    else:
        desired_size = y  # Set Max Image Dimension
        minimum_size - x

    if watermark != "null":
        watermark = Image.open(img_path+"/"+watermark)
        minimum_size = int((minimum_size*watermark_size)/100)
        watermark_margin = int(minimum_size*watermark_size/100)
        position = position

        watermark_resized = watermark.resize((minimum_size, minimum_size))

        if position == "br":
            position = (x - watermark_margin - watermark_resized.width,
                        y - watermark_margin - watermark_resized.height)
        elif position == "bl":
            position = (0 + watermark_margin, y -
                        watermark_margin - watermark_resized.height)
        elif position == "tr":
            position = (x - watermark_margin -
                        watermark_resized.width, 0 + watermark_margin)
        elif position == "tl":
            position = (0 + watermark_margin, 0 + watermark_margin)
        else:
            position_one = (im.width - watermark_resized.height) - \
                int((im.width - watermark_resized.height)*watermark_margin/100)
            position_two = (im.height - watermark_resized.width) - \
                int((im.height - watermark_resized.width)*watermark_margin/100)
            position = position_one, position_two

        im.paste(watermark_resized, position, watermark_resized)

    old_size = im.size          # old_size[0] is in (width, height) format

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    im = im.resize(new_size, Image.ANTIALIAS)
    #Color Picker
    color = color 
    if color == "thief":
        color_thief = ColorThief(im_pth)
        color = color_thief.get_color(quality=1)
    if re.findall('#\w*',filename):
        color= re.findall('#\w*',filename)[0]
    if file_extension != ".png":
        fill_color = color
        new_im = Image.new("RGB", (desired_size, desired_size), fill_color)

    else:
        fill_color = color
        new_im = Image.new("RGBA", (desired_size, desired_size), fill_color)
        bg = Image.new("RGBA",(x,y),fill_color)
        im = Image.alpha_composite(bg,im)

    new_im.paste(im, ((desired_size-new_size[0])//2, (desired_size-new_size[1])//2))

    if os.path.exists(img_path+"/picToSquare/"):
        pass
    else:
        os.makedirs(img_path+"/picToSquare/")

    new_im.save(img_path+"/picToSquare/"+filename)
