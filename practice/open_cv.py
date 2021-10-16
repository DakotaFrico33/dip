#!/usr/bin/env python3
import cv2

def put_text(img, title='image', xy=(5,20), font=cv2.FONT_HERSHEY_SIMPLEX,scale=0.7,bgr=(255,255,255),th=2):
    str = f"{title}"
    cv2.putText(img, str, (xy[0], xy[1]), font, scale, bgr)
    return img

#
# def read_key(key,k):
#     if key == ord('q'):
#         cv2.destroyAllWindows()
#         return 0
#     elif key == ord('.'):
#         k = k+offset
#     elif key == ord(','):
#         k = k-offset
#         if k<0:
#             return -1
#     return k
#

def read_key(key,k1=1,k2=999,k3=999,offset=2):
    if key == ord('q'):
        cv2.destroyAllWindows()
        k1=-2
    elif key == ord('a'):
        k1 = k1+offset
    elif key == ord('s'):
        k2 = k2+offset
    elif key == ord('d'):
        k3 = k3+offset
    elif key == ord('z'):
        k1 = k1-offset
    elif key == ord('x'):
        k2 = k2-offset
    elif key == ord('c'):
        k3 = k3-offset
    return k1,k2,k3
