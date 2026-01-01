
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

#to capture images and save when clicked
folder = "sign/X"
counter = 0


#this is for camera to recognize and resizing the hand gesture on h,w
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        
        
        imgcrop = img[y-offset : y+h+offset , x-offset : x+w+offset ]
        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        
        imgCropShape = imgcrop.shape
        
        
        aspectRatio = h/w 
        if aspectRatio > 1:
            k = imgSize/h
            wCal = math.ceil(k*w) 
            imgResize = cv2.resize(imgcrop , (wCal , imgSize ))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[ : , wGap : wCal+wGap] = imgResize
            
            
            
        else:
            k = imgSize/w
            hCal = math.ceil(k*h) 
            imgResize = cv2.resize(imgcrop , (imgSize , hCal ))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[ hGap : hCal + hGap, : ] = imgResize
            
        
        
        
        
        cv2.imshow('ImageCrop' , imgcrop)
        cv2.imshow('ImgWhite' , imgWhite)
    
    
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)