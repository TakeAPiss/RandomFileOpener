import os, random

folder=r"" #This is where you put your Folder Path

a=random.choice(os.listdir(folder))
print(a)

#os.open(a, os.O_RDWR)
from PIL import Image
file = folder+'\\'+a
Image.open(file).show()