
# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math
import video

if __name__ == '__main__':
    print(__doc__)

    try:
        fn = sys.argv[1]
    except IndexError:
        fn = 0

    def nothing(*arg):
        pass

    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 40, 100, nothing)
    cv2.createTrackbar('thrs2', 'edge', 70, 100, nothing)
    cv2.createTrackbar('thrs3', 'edge', 3, 10, nothing)

    cap = video.create_capture(fn)
    while True:
        flag, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thrs1 = cv2.getTrackbarPos('thrs1', 'edge') # threshold
        thrs2 = cv2.getTrackbarPos('thrs2', 'edge') # min line length
        thrs3 = cv2.getTrackbarPos('thrs3', 'edge') # max line gap
        edge = cv2.Canny(gray, 50, 200, apertureSize=5)
        lines = cv2.HoughLinesP(edge, 1, math.pi/180.0, thrs1, np.array([]), thrs2, thrs3)
        if lines is not None:
            a,b,c = lines.shape
            for i in range(a):
                cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
        ch = cv2.waitKey(5) & 0xFF
        cv2.imshow('edge',img)
        if ch == 27:
            break
    cv2.destroyAllWindows()
