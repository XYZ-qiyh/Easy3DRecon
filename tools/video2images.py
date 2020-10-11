import os
import cv2
import argparse

if __name__ == "__main__":
    # parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", type=str, help="the path of video to be processed")
    parser.add_argument("--sample_interval", type=int, default=0, help="sample intervel")
		
    args = parser.parse_args()
    video_path = args.video_path
    sample_interval = args.sample_interval
	
    # mkdir for images
    output_folder = os.path.splitext(video_path)[0]
    print("output_folder: {}".format(output_folder))
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
	
    cap = cv2.VideoCapture(video_path)
	
    idx = 0
    out_idx = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        #print("ret: {}".format(ret))
        if (ret == True):
            if (idx % (sample_interval+1) == 0):
                filename = os.path.join(output_folder, '{:0>8}.jpg'.format(out_idx))
                cv2.imwrite(filename, frame)
                out_idx = out_idx + 1
        else:
            break # No frame
        idx = idx + 1
        #print("idx: {}".format(idx))

    cap.release()
	
    print("saved {} frames.".format(out_idx))
