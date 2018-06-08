#!/usr/bin/python3
from darknet import detect
import cv2
import os
import argparse

def run_video(video_in, video_out):
    cap = cv2.VideoCapture(video_in)
    #find the opencv version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver) < 3:
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        width = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(video_out, fourcc, fps, (int(width), int(height)))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret==False: break
        
        cv2.imwrite("/dev/shm/frame.png", frame)
        
        predictions = detect("/dev/shm/frame.png")
       
        for box in predictions:
            label, confidence, position = box
            if label!="traffic light": continue

            x, y, w, h = position
            x1, y1 = int(x - w/2), int(y - h/2)
            x2, y2 = int(x + w/2), int(y + h/2)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 1)
        
        out.write(frame)
        cv2.imshow("video", frame)
        
        key = cv2.waitKey(1) or 0xFF
        if key == ord("q"):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return 0;

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=False, help="path to input video")
    ap.add_argument("-o", "--output", required=True, help="path to output video")
    args = vars(ap.parse_args())

    if args["input"] == None:
        video_in = 0
    else:
        video_in = args["input"]
    video_out = args["output"]

    run_video(video_in, video_out)
