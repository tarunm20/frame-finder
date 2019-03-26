import cv2
import numpy as np
import os
from pathlib import Path

vid = cv2.VideoCapture('video.ts')

try:
    if not os.path.exists('frames'):
        os.makedirs('frames')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0

while(True):

    grabbed,frame = vid.read()

    if not grabbed:
        break

    dir = './frames/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + dir)
    cv2.imwrite(dir, frame)


    currentFrame += 1

vid.release()
cv2.destroyAllWindows()
