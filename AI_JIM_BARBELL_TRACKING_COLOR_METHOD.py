# -*- coding: utf-8 -*-
"""
@author: computervisioneng

https://github.com/computervisioneng
Este codigo ha sido propocionado por el usuario 
Computer vision engineer en Github

Y ha sido modificado por mi, Nicolas GTarrio, para adapatarlo a mi caso


"""
import cv2
from PIL import Image

from util import get_limits


red = [0, 0, 255]  # Rojo en codigo BGR
cap = cv2.VideoCapture(2)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=red)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
