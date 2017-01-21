#!/usr/bin/env python

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

#    cap = video.create_capture(fn)
    while True:
#        flag, img = cap.read()
        img=cv2.imread("board.jpg")
        cv2.imshow('a', img)
        cv2.waitKey()
        img=cv2.imread("pic1.png")
        cv2.imshow('a', img)
        cv2.waitKey()
        ch = cv2.waitKey(5) & 0xFF
        if ch == 27:
            break
        
    cv2.destroyAllWindows()
