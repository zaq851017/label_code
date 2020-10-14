import argparse
import os
def LISTDIR(path):
    out = os.listdir(path)
    out.sort()
    return out
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path",type=str, default='')
    config = parser.parse_args()
    for dirfile in LISTDIR(config.video_path):
        full_file = os.path.join(config.video_path, dirfile)
        for real_file in LISTDIR(full_file):
            full_file_2 = os.path.join(full_file, real_file)
            print("cp -r "+full_file_2+" video_train_dataset")
            os.system("cp -r "+full_file_2+" video_train_dataset")
