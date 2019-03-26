import cv2
import numpy as np
import os, os.path
from random import randint

reference = cv2.imread('trial1.jpg')
listOfFrames = os.listdir('frames')
frame_list = []

for frame in listOfFrames:
    fullPath = os.path.join('/frames',frame)
    frame_list.append(fullPath)

doppelganger = cv2.imread('trial2.jpg')

"""
for i in range(len(frame_list)-1):
    checking = cv2.imread('frames/frame'+str(i)+'.jpg')
    if reference.shape == checking.shape:
        dif = cv2.subtract(reference,checking)
        b,g,r = cv2.split(dif)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            doppelganger = cv2.imread('frames/frame'+str(i)+'.jpg')
            print('frames/frame'+str(i)+'.jpg')
            break

frame_time = None
with open('timestamps.csv','r') as f:
    for line in f:
        (frame,ms) = line.split(',')
        if frame == currentFrame:
            frame_time = ms
            break
print(frame_time)
"""

if reference.shape == doppelganger.shape:
    dif = cv2.subtract(reference,doppelganger)
    b,g,r = cv2.split(dif)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print('Both files are the same')
        
cv2.destroyAllWindows()
