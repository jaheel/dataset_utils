import os.path
from glob import glob

jpg_path = "./JPEGImages/"

files = glob(jpg_path + "*.jpg")
files = [i.split("\\")[-1].split(".jpg")[0] for i in files]
print(files)

for index in range(2200):
    if str(index).zfill(6) in files:
        pass
    else:
        print(index)