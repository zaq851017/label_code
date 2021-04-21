import cv2
import numpy as np
import colorList
import os
import logging
from tqdm import tqdm
import argparse
import ipdb
def LISTDIR(path):
    out = os.listdir(path)
    out.sort()
    return out

def scale_contour(cnt, scale):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cnt_norm = cnt - [cx, cy]
    cnt_scaled = cnt_norm * scale
    cnt_scaled = cnt_scaled + [cx, cy]
    cnt_scaled = cnt_scaled.astype(np.int32)

    return cnt_scaled

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path")
    args = parser.parse_args()
    for num_files in LISTDIR(args.input_path):
        full_path = os.path.join(args.input_path,num_files)
        for dir_files in LISTDIR(full_path):
            full_path_2 = os.path.join(full_path,dir_files)
            mask_path = os.path.join(full_path_2, "mask")
            origin_path = os.path.join(full_path_2, "original")
            heat_path = os.path.join(full_path_2, "heat")
            polygon_path = os.path.join(full_path_2, "polygon")
            print(full_path_2)
            if not os.path.isdir(polygon_path):
                os.makedirs(polygon_path)
            for files in LISTDIR(origin_path):
                origin_files = os.path.join(origin_path, files)
                mask_files = os.path.join(mask_path, files.split(".")[0]+"_out.jpg")
                img = cv2.imread(origin_files)
                mask = cv2.imread(mask_files)
                mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY) 
                ret, mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)  
                contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                if contours != []:
                    cnt_scaled = scale_contour(contours[0], 0.88)
                    cv2.drawContours(img, [cnt_scaled], 0, (0, 255, 0), 2)
                else:
                    cv2.drawContours(img, contours, 0, (0, 255, 0), 2)
                cv2.imwrite(os.path.join(polygon_path, files), img)
                """
                coef_y = img_orig.shape[0] / img_resized.shape[0]
                coef_x = img_orig.shape[1] / img_resized.shape[1]
                cv2.imwrite(os.path.join(heat_path, files), heat_img)
                """