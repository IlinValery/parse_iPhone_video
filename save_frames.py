import cv2
import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inf', type=str, help='input video path --inf', default='img.mp4')
    parser.add_argument('--fr', type=int, help='input frequency --fr', default=24)
    args = parser.parse_args()

    file_name = args.inf
    pic_name = str(file_name)
    pic_name = pic_name.split('.')[0]
    frequency = args.fr

    print(cv2.__version__)
    vidcap = cv2.VideoCapture(file_name)
    success,image = vidcap.read()
    count = 0
    rows, cols, chan = image.shape
    angle = 270
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

    print(rows, cols)
    success = True
    while success:
        success,image = vidcap.read()
        dst = cv2.warpAffine(image, M, (rows,cols))
        img90 = np.rot90(image)
        img180 = np.rot90(img90)
        img270 = np.rot90(img180)
        #print('Read a frame %d: ' % count, success)
        if count%frequency==0:
            cv2.imwrite("%(file_name)s_%(number)d.jpg" % {"file_name": pic_name, "number": count}, img270)    # save frame as JPEG file
            print("Frame %(number)d was saved as %(file_name)s%(number)d.jpg!" % {"file_name": pic_name, "number": count})
        count += 1

if __name__ == "__main__":
  main()
