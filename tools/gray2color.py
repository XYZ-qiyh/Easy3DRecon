import cv2
import argparse
import sys
sys.path.append("../")

from datasets.data_io import read_pfm, write_depth_img

if __name__ == "__main__":
    # parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument("depth_path")
    args = parser.parse_args()
    depth_path = args.depth_path
    
    # read_pfm 
    depth_map, _ = read_pfm(depth_path)
    
    # photometric filter
    if False:
        pfm_prob_path = depth_path.replace("depth_est", "confidence")
        prob_map, _ = read_pfm(pfm_prob_path)
        depth_map[prob_map < 0.9] = 0
    
    # gray2color
    write_depth_img(depth_path.replace(".pfm", ".jpg"), depth_map, color=True)
