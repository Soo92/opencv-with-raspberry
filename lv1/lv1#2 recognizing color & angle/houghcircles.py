# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys

if __name__ == '__main__':
    print(__doc__)

    fn = "straight.jpg"

    while True:
        src = cv2.imread(fn, 1)
        img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 5)
        row,col,ch=src.shape
        cimg = src.copy() # numpy function
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)
        if circles is not None:
            a, b, c = circles.shape
            if b>2:
                for i in range(b):
                    cv2.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
                    print(cimg[circles[0][i][1],circles[0][i][0]])
        cv2.imshow("detected circles", cimg)
        ch = cv2.waitKey(0) & 0xFF
        if ch == ord('a'):
            fn="straight.jpg"
            print('straight')
        if ch == ord('s'):
            fn="left.jpg"
            print('left')
        if ch == ord('d'):
            fn="right.jpg"
            print('right')
        if ch == 27:
            break
    cv2.destroyAllWindows()
