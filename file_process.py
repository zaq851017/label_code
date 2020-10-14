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

def CHECK_DSSTORE(path):
    if path == ".DS_Store" or path =="video":
        return True
    else:
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path",type=str, default='./after_process_data/')
    parser.add_argument("--mode",type=str, default='train')
    args = parser.parse_args()
    """
    if not os.path.isdir('./train_dataset/'):
        os.makedirs("./train_dataset/")  
    """
    if args.mode == "train":
        for num_files in LISTDIR(args.data_path):
            full_path = os.path.join(args.data_path,num_files)
            if os.path.isdir(full_path):
                for dir_files in LISTDIR(full_path):
                    full_path_2 = os.path.join(full_path,dir_files)
                    mask_list = []
                    original_list = []
                    if os.path.isdir(full_path_2):
                        all_mask = 0
                        all_origin = 0
                        for frame_files in (LISTDIR(full_path_2)):
                            if frame_files == "mask":
                                full_path_3 = os.path.join(full_path_2,frame_files)
                                for real_frame_files in tqdm(LISTDIR(full_path_3)):
                                    real_frame_files[5:8]
                                    if CHECK_DSSTORE(real_frame_files):
                                        continue
                                    full_path_4 = os.path.join(full_path_3,real_frame_files)
                                    os.system("cp "+full_path_4+" ./train_dataset/masks/"+num_files+"_"+dir_files+"_"+real_frame_files[:-8]+".jpg")
                                    all_mask += int(real_frame_files[5:8])
                            elif frame_files == "original":
                                full_path_3 = os.path.join(full_path_2,frame_files)
                                for real_frame_files in tqdm(LISTDIR(full_path_3)):
                                    if CHECK_DSSTORE(real_frame_files):
                                        continue
                                    full_path_4 = os.path.join(full_path_3,real_frame_files)
                                    os.system("cp "+full_path_4+" ./train_dataset/images/"+num_files+"_"+dir_files+"_"+real_frame_files)
                                    all_origin += int(real_frame_files[5:8])
                        print("path : ",full_path_2)
                        print("two num distance is(original - mask):",all_origin-all_mask)
    if args.mode == "test":
        for num_files in LISTDIR(args.data_path):
            full_path = os.path.join(args.data_path,num_files)
            if os.path.isdir(full_path):
                for dir_files in LISTDIR(full_path):
                    full_path_2 = os.path.join(full_path,dir_files)
                    mask_list = []
                    original_list = []
                    if os.path.isdir(full_path_2):
                        all_mask = 0
                        all_origin = 0
                        for frame_files in (LISTDIR(full_path_2)):
                            if frame_files == "mask":
                                full_path_3 = os.path.join(full_path_2,frame_files)
                                for real_frame_files in tqdm(LISTDIR(full_path_3)):
                                    real_frame_files[5:8]
                                    if CHECK_DSSTORE(real_frame_files):
                                        continue
                                    full_path_4 = os.path.join(full_path_3,real_frame_files)
                                    os.system("cp "+full_path_4+" ./test_dataset/masks/"+num_files+"_"+dir_files+"_"+real_frame_files[:-8]+".jpg")
                                    all_mask += int(real_frame_files[5:8])
                            elif frame_files == "original":
                                full_path_3 = os.path.join(full_path_2,frame_files)
                                for real_frame_files in tqdm(LISTDIR(full_path_3)):
                                    if CHECK_DSSTORE(real_frame_files):
                                        continue
                                    full_path_4 = os.path.join(full_path_3,real_frame_files)
                                    os.system("cp "+full_path_4+" ./test_dataset/images/"+num_files+"_"+dir_files+"_"+real_frame_files)
                                    all_origin += int(real_frame_files[5:8])
                        print("path : ",full_path_2)
                        print("two num distance is(original - mask):",all_origin-all_mask)
                            
