import cv2
import numpy as np
import random
import time

def perspectimg(image, pts1, pts2):
# pts1.shape = [4, 2]
# pts2.shape = [4, 2]
    h, w = image.shape[:2]
    H = cv2.getPerspectiveTransform(pts1.astype(np.float32), pts2.astype(np.float32))
    out = cv2.warpPerspective(image, H, (2*w, 2*h))
    return out

if __name__ == '__main__':
    img = cv2.imread('test.jpg')
    # img = cv2.imread('test2.png')
    p3 = np.float32([[25, 25], [199, 25], [199, 199], [25, 199]])
    p4 = np.float32([[45, 25], [205, 65], [204, 194], [49, 230]])
    img = perspectimg(img, p3, p4)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    QRmodel = cv2.QRCodeDetector()
    start = time.time()
    codeinfo, pts, outs = QRmodel.detectAndDecode(img)
    end = time.time()
    print('time usage: ', end - start)
    print(codeinfo, pts)
    cv2.drawContours(img, [np.int32(pts[0])], -1, (0, 0, 255), 2)
    cv2.imshow('QR', img)
    cv2.imshow('straight_QR', outs)
    cv2.waitKey(0)
    # time usage:  0.011999130249023438
    # Hello :) [[[ 43.908947  24.221338]
    #  [203.97652   64.5437  ]
    #  [206.06259  193.88025 ]
    #  [ 48.87426  230.28175 ]]]
