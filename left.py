import os

with open("classes_og.txt", "r") as f:
    data = f.readlines()

nwFiles = os.listdir("images")
oldFiles = []

for line in data:
    words = line.split()
    oldFiles.append(words[0])
for fl in nwFiles:
    if not fl in oldFiles:
        print(fl)
