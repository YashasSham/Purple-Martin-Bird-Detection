# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:58:23 2018

@author: Yasha
"""

import cv2    #(openCV import)
import math
import predict

def video_proccessing(video_name):
    vidcap = cv2.VideoCapture(video_name)
    success,image = vidcap.read()
    
    frameRate = vidcap.get(5)
    image_size=128
    num_channels=3
    images = []
    while(vidcap.isOpened()):
        frameId = vidcap.get(1) #current frame number
        ret, frame = vidcap.read()
        
        if (ret != True):
            break
        if (frameId % math.floor(frameRate) == 0):
            #filename = str(int(frameId)) + ".jpg"
            #cv2.imwrite(filename,frame)
            n = cv2.resize(frame, (image_size, image_size), cv2.INTER_AREA)
            images.append(n)
    vidcap.release()
    result, prediction = predict.predict_video(images,image_size,num_channels)
    
    return result, prediction