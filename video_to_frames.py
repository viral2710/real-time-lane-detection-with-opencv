import cv2
import os
vidcap = cv2.VideoCapture('test.mp4')
path=r'C:/Users/viral/Desktop/final project/Finding_Lane_Lines/test'
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        img = image[0:540, 0:1280]
        cv2.imwrite(os.path.join(path , str(count)+".jpg"), img)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.05 #it will capture image in each 0.5 second
count=0
success = getFrame(sec)
while success:
    print(count)
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    count = count + 1
