from os import listdir, remove, scandir
from PIL import Image
from tqdm import tqdm

Image.MAX_IMAGE_PIXELS = 93312000000

subfolders = [ f.path for f in scandir("images/") if f.is_dir() ]

for folder in subfolders:
    print("Verify "+folder)
    for filename in tqdm(listdir(folder)):
        if filename.endswith('.jpg'):
            try:
                img = Image.open(folder+"/"+filename) # open the image file
                img.verify() # verify that it is, in fact an image
            except (IOError, SyntaxError) as e:
                print("removing", folder+"/"+filename)
                remove(''+folder+"/"+filename)