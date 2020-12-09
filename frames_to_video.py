import cv2
import numpy as np
import os
from os.path import isfile, join
pathIn= r'C:Users/viral/Desktop/final project/data/'
pathOut = 'video1.mp4'
fps = 30
frame_array = []
DATA_FOLDER = "C:/Users/viral/Desktop/final project/data"
DATA_FILE = os.path.join(DATA_FOLDER, "data1.txt")
x = []
with open(DATA_FILE) as f:
    for line in f:
        image_name, angle,_,_ = line.split()
        
        image_path = os.path.join(DATA_FOLDER, image_name)
        x.append(image_path)
for i in x:
    #reading each files
    img = cv2.imread(i)
    print(i)
    height=img.shape[0]
    width=img.shape[1]
    layer=img.shape[2]
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()