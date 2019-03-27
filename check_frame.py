import cv2
import numpy as np
import os, os.path
from random import randint

reference = cv2.imread('image.jpg')
listOfFrames = os.listdir('frames')
frame_list = []

for frame in listOfFrames:
    fullPath = os.path.join('/frames',frame)
    frame_list.append(fullPath)

doppelganger = None
count = -1
for i in range(len(frame_list)-1):
    checking = cv2.imread('frames/frame'+str(i)+'.jpg')
    if reference.shape == checking.shape:
        dif = cv2.subtract(reference,checking)
        b,g,r = cv2.split(dif)
        count += 1
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            doppelganger = cv2.imread('frames/frame'+str(i)+'.jpg')
            print('frames/frame'+str(i)+'.jpg')
            break

frame_time = None
f = open("timestamps.csv","r")
for line in f:
    (frame,ms) = line.split(',')
    if frame == str(count):
        frame_time = ms
        f.close()
        break
print(frame_time)

cv2.destroyAllWindows()
