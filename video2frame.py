import cv2
import numpy as np
import colorList
import os
import logging
from tqdm import tqdm
import argparse
import ipdb

if __name__ == "__main__":
    vidcap = cv2.VideoCapture("temp.avi")
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        if count<10:
            cv2.imwrite("temp_out/frame00%d.jpg" % count, image) 
        elif count < 100 and count > 9:
            cv2.imwrite("temp_out/frame0%d.jpg" % count, image)
        elif count > 99: 
            cv2.imwrite("temp_out/frame%d.jpg" % count, image)
        count += 1 
        success,image = vidcap.read()