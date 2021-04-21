import cv2
import numpy as np
import colorList
import os
import logging
from tqdm import tqdm
import argparse
import ipdb
import colorList
def LISTDIR(path):
    out = os.listdir(path)
    out.sort()
    return out
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path")
    args = parser.parse_args()
    for files in LISTDIR(args.input_path):
        full_path = os.path.join(args.input_path, files)
        merge_path = os.path.join(full_path, "merge")
        repolygon_path = os.path.join(full_path, "repolygon")
        for img_files in LISTDIR(merge_path):
            img_path = os.path.join(merge_path, img_files)
            left_img = cv2.imread(img_path)[:,:720,:]
            hsv = cv2.cvtColor(left_img,cv2.COLOR_BGR2HSV)
            color_dict = colorList.getColorList()
            cv2.imwrite(os.path.join(repolygon_path, img_files), left_img)
            for color_which,d in enumerate(color_dict):
                if color_which == 1:
                    green_mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])