import cv2
import numpy as np
import os, os.path

reference = cv2.imread('image.jpg')
listOfFrames = os.listdir('frames')
frame_list = []

for frame in listOfFrames:
    fullPath = os.path.join('/frames',frame)
    frame_list.append(fullPath)

doppelganger = None

"""
The section below is for finding the right frame and printing the timestamp 
for it but it doesn't work with the specific video and picture at the moment.
"""
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

cv2.destroyAllWindows()
