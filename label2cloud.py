import cv2
import numpy as np
import os
import argparse
from tqdm import tqdm

def LISTDIR(path):
    out = os.listdir(path)
    out.sort()
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path")
    parser.add_argument("--output_path",default="./my_label_data/")
    args = parser.parse_args()
    for num_files in LISTDIR(args.input_path):
        full_path = os.path.join(args.input_path,num_files)
        for dir_files in LISTDIR(full_path):
            full_path_2 = os.path.join(full_path, dir_files)
            os.makedirs(args.output_path + full_path_2)
            os.system("cp -r "+full_path_2+"/label " + args.output_path + full_path_2 + "/label")
            os.system("cp -r "+full_path_2+"/original "+ args.output_path + full_path_2 + "/original")

