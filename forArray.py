import os, subprocess, time

names = [

]
for name in names:
    print("calling "+"python .\\flickr_scraper.py --search '"+name+"' --n 1000 --download")
    subprocess.call("python .\\flickr_scraper.py --search '"+name+"' --n 1000 --download")