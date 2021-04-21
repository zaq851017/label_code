import cv2
import numpy as np
import os
import logging
from tqdm import tqdm
import argparse
import ipdb
import matplotlib.pyplot as plt
import imageio
def LISTDIR(path):
    out = os.listdir(path)
    out.sort()
    return out

if __name__ == "__main__":
    input_p = "./specific_correct_label"
    output_p = './specific_correct_label_result'
    for num_file in LISTDIR(input_p):
        full_path_i = os.path.join(input_p,num_file)
        full_path_o = os.path.join(output_p,num_file)
        for dir_file in LISTDIR(full_path_i):
            full_path_i_i = os.path.join(full_path_i, dir_file)
            full_path_o_o = os.path.join(full_path_o, dir_file)
            full_path_i_i_txt = os.path.join(full_path_i_i, "height.txt")
            full_path_o_o_txt = os.path.join(full_path_o_o, "height.txt")
            print("mv "+full_path_i_i_txt+" "+full_path_o_o_txt)
            os.system("mv "+full_path_i_i_txt+" "+full_path_o_o_txt)