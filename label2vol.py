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
def frame2video(path):
    video_path = (path[:-6])
    videoWriter = cv2.VideoWriter(os.path.join(video_path,"video.avi"), cv2.VideoWriter_fourcc(*'DIVX'), 12, (1440, 540))
    for frame_files in  LISTDIR(path):
        if frame_files[-3:] == "jpg":
            full_path = os.path.join(path, frame_files)
            frame = cv2.imread(full_path)
            videoWriter.write(frame)
    videoWriter.release()
def vol_cal(frame_file_path):
    pixel_area = (1 / 85)**2  # h = 10/85(mm)
    for num_files in LISTDIR(frame_file_path):
        full_path = os.path.join(frame_file_path, num_files)
        for date_file in LISTDIR(full_path):
            full_path_2 = os.path.join(full_path, date_file)
            height_file = os.path.join(full_path_2, "height.txt")
            f = open(height_file, "r")
            height = float(f.read())/10.0
            f.close()
            mask_path = os.path.join(full_path_2, "mask")
            origin_path = os.path.join(full_path_2, "original")
            if not os.path.isdir(os.path.join(full_path_2, "merge")):
                os.makedirs(os.path.join(full_path_2, "merge"))
            if not os.path.isdir(os.path.join(full_path_2, "forfilm")):
                os.makedirs(os.path.join(full_path_2, "forfilm"))
            mask_list = []
            print(mask_path)
            for mask_file in tqdm(LISTDIR(mask_path)):
                origin_file = mask_file.split("_")[0]+".jpg"
                full_path_3 = os.path.join(mask_path, mask_file)
                full_path_4 = os.path.join(origin_path, origin_file)
                mask = cv2.imread(full_path_3, cv2.IMREAD_GRAYSCALE)
                mask_list.append(mask)
                #ipdb.set_trace()
                mask [mask <= 127] = 0
                mask [mask > 128 ] = 1
                origin = cv2.imread(full_path_4)
                origin_draw_image = origin.copy()
                contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                maege_image = np.zeros( (origin.shape[0], origin.shape[1]*2,1),dtype=np.uint8)
                if contours ==[]:
                    maege_image = np.concatenate( (origin, origin_draw_image), axis = 1)
                    imageio.imwrite(os.path.join(os.path.join(full_path_2, "merge"), origin_file), maege_image)
                    imageio.imwrite(os.path.join(os.path.join(full_path_2, "forfilm"), origin_file), origin)
                else:
                    cv2.drawContours(np.uint8(origin_draw_image), contours, -1, (0,255,0), 3)
                    maege_image = np.concatenate( (origin, np.uint8(origin_draw_image)), axis = 1)
                    imageio.imwrite(os.path.join(os.path.join(full_path_2, "merge"), origin_file), maege_image)
                    imageio.imwrite(os.path.join(os.path.join(full_path_2, "forfilm"), origin_file), origin_draw_image)
            left_area = 0.0
            right_area = 0.0
            area = []
            index = []
            for i in range(0, len(mask_list)-1):
                left_area += np.count_nonzero(mask_list[i] != 0.0)
                temp_area = np.count_nonzero(mask_list[i] != 0.0) * pixel_area / len(mask_list)
                area.append(temp_area)
                index.append(i)
            temp_area = np.count_nonzero(mask_list[len(mask_list)-1] != 0.0) * pixel_area / len(mask_list)
            area.append(temp_area)
            index.append(len(mask_list))
            for i in range(1, len(mask_list)):
                right_area += np.count_nonzero(mask_list[i] != 0.0)    
            ll = (left_area * pixel_area)
            rr = (right_area * pixel_area)
            result = (ll+rr)*height/(2*len(mask_list))
            plt.title("Volume: "+str(round(result,4))+" ml")
            plt.xlabel("frame")
            plt.ylabel("area(cm^2)")
            plt.bar(index, area, width=1.0)
            #plt.show()
            save_path = os.path.join(full_path_2, "Volume.jpg")
            plt.savefig(save_path)
            plt.close()
    for dir_files in (LISTDIR("./specific_label/")):
        full_path = os.path.join("./specific_label/", dir_files)
        for num_files in tqdm(LISTDIR(full_path)):
            full_path_2 = os.path.join(full_path, num_files+"/merge")
            frame2video(full_path_2)
if __name__ == "__main__":
    vol_result = vol_cal("./specific_label/")