from PIL import Image, ImageDraw
import os, glob
from tqdm import tqdm

imdir = 'images/avocado'
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '/*.' + e)) for e in ext]
print("Converting "+str(len(files))+ " files")

#Check whether the folder doesn't already exist
if os.path.isdir(imdir+"/s/"):
    print("Folder already exists")
else:
    os.mkdir(imdir+"/s/")

i = 0

for image in tqdm(files):
    i += 1
    #Define input img
    im = Image.open(image).convert("RGB")
    basewidth = 512
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))

    formIndex = (4-len(str(i)))*"0"+str(i)
    #im_out = imdir+"/s/"+image.split('\\')[-1] #For keeping the file name¨

    im_out = imdir+"/s/"+str(formIndex)+".jpg"
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    im.save(im_out,optimize=True,quality=42) 