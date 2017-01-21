# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math

def angle(dx,dy):
    return math.atan2(dy,dx)*180/math.pi

if __name__ == '__main__':
    print(__doc__)

    fn = "straight.jpg"

    while True:
        src = cv2.imread(fn)
        dst = cv2.Canny(src, 10, 50)
        row,col,ch=src.shape

        lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 40, np.array([]), 50, 10)
        if lines is not None:
            a,b,c = lines.shape
            (d,e)=(row/2,row/2)
            (f,g)=(-1,-1)
            for i in range(a):
                (x1,y1,x2,y2)=(lines[i][0][0],lines[i][0][1],lines[i][0][2],lines[i][0][3])
                if max(y1,y2)>row/2 and min(x1,x2)<col/2 and angle(x2-x1,y2-y1)<0 and max(y1,y2)>d:
                    d=max(y1,y2)
                    f=i
                if max(y1,y2)>row/2 and max(x1,x2)>col/2 and angle(x2-x1,y2-y1)>0 and max(y1,y2)>e:
                    e=max(y1,y2)
                    g=i
            if f != -1:
                (x1,y1,x2,y2)=(lines[f][0][0],lines[f][0][1],lines[f][0][2],lines[f][0][3])
                print ("left side angle is",angle(x2-x1,y2-y1))
                cv2.line(src, (x1,y1),(x2,y2), (0, 0, 255), 3, cv2.LINE_AA)
            if g != -1:
                (x1,y1,x2,y2)=(lines[g][0][0],lines[g][0][1],lines[g][0][2],lines[g][0][3])
                print ("right side angle is",angle(x2-x1,y2-y1))
                cv2.line(src, (x1,y1),(x2,y2), (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow("detected lines", src)
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
