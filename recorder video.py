# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:32:20 2023

@author: Ashu
"""

import cv2 as c 
import numpy as np
import pyautogui as p 

#Create Resolution 

rs= p.size()

#filename in which we store recording
fn=input("Please enter any file name and path: ")

#fix the frame rate
fps=30.0

fourcc=c.VideoWriter_fourcc(*"XVID")
output=c.VideoWriter(fn, fourcc, fps, rs)

#Create recording module
c.namedWindow("Live_Recording", c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording", (640,640))

while True:
    img=p.screenshot()
    f=np.array(img)
    f=c.cvtColor(f,c.COLOR_RGB2BGR)
    output.write(f)
    c.imshow("Live_Recording", f)
    if c.waitKey(1) & 0xFF==ord("q"):
        break

output.release()
c.destroyAllWindows()
