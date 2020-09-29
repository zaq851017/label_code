import cv2
import numpy as np
import colorList
import os
import logging
from tqdm import tqdm
import argparse
def get_color(frame):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    color_dict = colorList.getColorList()
    yellow_point_num = 0
    green_point_num = 0
    yellow_point_list = []
    green_point_list = []
    for color_which,d in enumerate(color_dict):
        if color_which == 0:
            yellow_mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])
            cv2.imwrite('yellow.jpg',yellow_mask)
            for i in range(yellow_mask.shape[0]):
                for j in range(yellow_mask.shape[1]):
                    if yellow_mask[i][j] == 255:
                        yellow_point_num +=1
                        yellow_point_list.append([j,i])
        if color_which == 1:
            green_mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])
            cv2.imwrite('green.jpg',green_mask)
            for i in range(green_mask.shape[0]):
                for j in range(green_mask.shape[1]):
                    if green_mask[i][j] == 255:
                        green_point_num +=1
                        green_point_list.append([j,i])
    if yellow_point_num >= green_point_num:
        logging.info("yellow")
        return yellow_mask,np.array(yellow_point_list)
    else:
        logging.info("green")
        return green_mask,np.array(green_point_list)

def LISTDIR(path):
    out = os.listdir(path)
    out.sort()
    return out

def CHECK_DSSTORE(path):
    if path == ".DS_Store" or path =="video":
        return True
    else:
        return False
        
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path")
    parser.add_argument("--output_path")
    args = parser.parse_args()
    for num_files in LISTDIR(args.input_path):
        full_path = os.path.join(args.input_path,num_files)
        out_file_path = os.path.join(args.output_path,num_files)
        if os.path.isdir(full_path): 
            for dir_files in LISTDIR(full_path):
                full_path_2 = os.path.join(full_path,dir_files)
                out_file_path_1 = os.path.join(out_file_path,dir_files)
                if os.path.isdir(full_path_2):
                    if not os.path.isdir(out_file_path):
                        os.makedirs(out_file_path_1)
                    for frame_files in tqdm(LISTDIR(full_path_2)):
                        if CHECK_DSSTORE(frame_files):
                            continue
                        full_path_3 = os.path.join(full_path_2,frame_files)
                        img_out_file_path = os.path.join(out_file_path_1,frame_files[:-4])
                        img_out_file_path = img_out_file_path + "_out.jpg"
                        logging.info("full_path: "+full_path_3)
                        logging.info("output_path:"+img_out_file_path)
                        frame = cv2.imread(full_path_3)
                        gs_img,point_list = get_color(frame)
                        if point_list.size != 0:
                            cv2.fillPoly(gs_img,[point_list],255) 
                            cv2.imwrite(img_out_file_path,gs_img)
                        else:
                            cv2.imwrite(img_out_file_path,gs_img)