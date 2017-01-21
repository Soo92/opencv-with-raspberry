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

    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
    cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)
    cv2.namedWindow('img')
    cv2.namedWindow('gray')
    cv2.namedWindow('vis')
    cv2.moveWindow('img',0,0)
    cv2.moveWindow('gray',0,700)
    cv2.moveWindow('edge',700,0)
    cv2.moveWindow('vis',700,700)
    cap = video.create_capture(fn)
    while True:
        flag, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
        thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
        vis = img.copy()
        vis = np.uint8(vis/2.)
        vis[edge != 0] = (0, 255, 0)
        cv2.imshow('img', img)
        cv2.imshow('gray', gray)
        cv2.imshow('edge', edge)
        cv2.imshow('vis', vis)
        ch = cv2.waitKey(5) & 0xFF
        if ch == 27:
            break
    cv2.destroyAllWindows()
