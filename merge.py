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
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path")
    args = parser.parse_args()
    for dir_files in LISTDIR(args.input_path):
        full_path = os.path.join(args.input_path, dir_files, "original")
        full_path_2 = os.path.join(args.input_path, dir_files, "heat")
        merge_path = os.path.join(args.input_path, dir_files, "merge")
        if not os.path.isdir(merge_path):
            os.makedirs(merge_path)
        for o_files in LISTDIR(full_path):
            origin_path = os.path.join(full_path, o_files)
            heat_path = os.path.join(full_path_2, o_files)
            write_path = os.path.join(merge_path, o_files)
            heat_img = cv2.imread(heat_path)
            origin_img = cv2.imread(origin_path)
            merge_img = np.hstack([origin_img, heat_img])
            cv2.imwrite(write_path, merge_img)