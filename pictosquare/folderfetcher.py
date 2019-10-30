import os
from pictosquare import imagesquarer
import re
import time
from tqdm import tqdm

def folderSquarer(user_directory, color):
    directory_to_scrap = user_directory
  
    if directory_to_scrap == "currentdir":
        directory_to_scrap = os.curdir
    elif os.path.exists(directory_to_scrap):
        directory_to_scrap = user_directory
    else:
        print("Directory Not Found")
    watermark_img = ""
    watermark_size = ""
    position = ""
    #Scan Directory 
    directory = os.listdir(directory_to_scrap)
    #Finding Watermark
    for watermark in directory:
        if watermark.startswith("watermark"): 
            watermark_img = watermark
            if watermark.endswith("br.png"):
                position = "br"
            elif watermark.endswith("tr.png"):
                position = "tr"
            elif watermark.endswith("bl.png"):
                position = "bl"
            elif watermark.endswith("tl.png"):
                position = "tl"
            else:
                position = "bl"
            try:
                watermark_size = int(re.findall('\d+',watermark)[0])
            except IOError:
                watermark_size = 10
            print(watermark_size)
            break
        else: 
            watermark_img = "null"    #Square Images In Folder
    print("Experimental Watermark Is Set To: "+watermark_img)
    #Sending Watermark URL to Main Images Squarer Script.
    print("Primary Background Color Is Set To: "+color)
    final_directory = []
    for image in directory:
        if image == watermark:
            continue
        if image.endswith("png") or image.endswith("jpg") or image.endswith("jpeg"):
            final_directory.append(image)      
    for image_file in tqdm(final_directory):
        imagesquarer.imageSquare(directory_to_scrap,image_file,watermark_img, position, watermark_size,color)         
        time.sleep(0.25)
        tqdm.write("picToSquare Is Resizing: " + image_file)

    print("Task complete.")
    print("Export Directory Is: "+ directory_to_scrap +"\picToSquare")    

