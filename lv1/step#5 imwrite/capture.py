# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

# relative module
import video

# built-in module
import sys


if __name__ == '__main__':
    print(__doc__)

    try:
        fn = sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    cap = video.create_capture(fn)
    while True:
        flag, img = cap.read()
        cv2.imshow('img', img)
        ch = cv2.waitKey(5) & 0xFF
        if ch == 27:
            break
        if ch == ord('a'):
            cv2.imwrite('straight.jpg',img)
            print("straight is captured")
        if ch == ord('s'):
            cv2.imwrite('right.jpg',img)
            print("right is captured")
        if ch == ord('d'):
            cv2.imwrite('left.jpg',img)
            print("left is captured")
    cv2.destroyAllWindows()
