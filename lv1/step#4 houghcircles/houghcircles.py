
# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
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
    cv2.createTrackbar('thrs1', 'edge', 7, 10, nothing)
    cv2.createTrackbar('thrs2', 'edge', 20, 50, nothing)

    cap = video.create_capture(fn)
    while True:
        flag, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
        thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
        circles = cv2.HoughCircles(edge, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, thrs1, thrs2)
        if circles is not None:
            a, b, c = circles.shape
            for i in range(b):
                cv2.circle(img, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv2.LINE_AA)
        cv2.imshow("edge", img)
        ch = cv2.waitKey(5) & 0xFF
        if ch == 27:
            break
    cv2.destroyAllWindows()
