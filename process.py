import cv2
import numpy as np
import os
import argparse
from tqdm import tqdm

def frametovideo(path):
    #frame_array = []
    #files = [f for f in os.listdir(path) if os.isfile(os.join(pathIn, f))]
    pass
def LISTDIR(path):
    out = os.listdir(path)
    out.sort()
    return out
def CHECK_DSSTORE(path):
    if path == ".DS_Store":
        return True
    else:
        return False

def LIST_IMG(left_path,right_path):
    left_img = LISTDIR(left_path)
    right_img = LISTDIR(right_path)
    return left_img,right_img

def MERGE_IMAGE(num,left_i,right_i,save_path):
    left = cv2.imread(left_i)
    right = cv2.imread(right_i)
    height = left.shape[0]
    width = left.shape[1]
    new_img = np.zeros([left.shape[0],left.shape[1]*2,3],np.uint8)
    new_img[:,0:width,:] = left
    new_img[:,width:,:] = right
    if num <10:
        cv2.imwrite(save_path+"/frame00"+str(num)+".jpg",new_img)
    elif num <100:
        cv2.imwrite(save_path+"/frame0"+str(num)+".jpg",new_img)
    elif num<1000:
        cv2.imwrite(save_path+"/frame"+str(num)+".jpg",new_img)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path")
    parser.add_argument("--merge_image",default="True")
    args = parser.parse_args()
    for num_files in LISTDIR(args.path):
        full_path = os.path.join(args.path,num_files)
        if os.path.isdir(full_path):
            for dir_files in LISTDIR(full_path):
                full_path_2 = os.path.join(full_path,dir_files)
                if os.path.isdir(full_path_2):
                    print(full_path_2)
                    right_path = os.path.join(full_path_2,"forfilm")
                    left_path = os.path.join(full_path_2,"test_o")
                    save_img_path = os.path.join(full_path_2,"merge_image")
                    video_path = os.path.join(full_path_2,"video")
                    if args.merge_image == "True":
                        if os.path.isdir(video_path):
                            os.system("rm -f -r "+video_path)
                            os.system("rm -f -r "+save_img_path)
                        os.system("mkdir -p "+save_img_path)
                        os.system("mkdir -p "+video_path)
                        left_img , right_img = LIST_IMG(left_path,right_path)
                        for i in range(len(left_img)):
                            MERGE_IMAGE(i,os.path.join(left_path,left_img[i]),os.path.join(right_path,right_img[i]),save_img_path)
                        os.system("rm -r -f "+right_path)
                        os.system("rm -r -f "+left_path)
                    for frame_files in LISTDIR(save_img_path):                     
                        full_path_3 = os.path.join(save_img_path,frame_files)
                        if CHECK_DSSTORE(frame_files):
                            os.system("rm -f -r "+full_path_3)
                            continue
                        frame = cv2.imread(full_path_3)
                        size = (frame.shape[1],frame.shape[0])
                        break
                    videoWriter = cv2.VideoWriter(full_path_2+"/video/"+dir_files+".avi", cv2.VideoWriter_fourcc(*'DIVX'), 12, size)
                    for frame_files in tqdm(LISTDIR(save_img_path)):
                        full_path_3 = os.path.join(save_img_path,frame_files)
                        if CHECK_DSSTORE(frame_files):
                            os.system("rm -f -r "+full_path_3)
                            continue
                        frame = cv2.imread(full_path_3)
                        videoWriter.write(frame)
                    videoWriter.release()


    