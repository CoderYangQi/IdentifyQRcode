import sys,os,time
import cv2

def displayBbox(im, bbox):
    if bbox is not None:
        bbox = [bbox[0].astype(int)]
        n = len(bbox[0])
        for i in range(n):
            cv2.line(im, tuple(bbox[0][i]), tuple(bbox[0][(i+1) % n]), (0,255,0), 3)

model_root = "opencv_3rdparty-wechat_qrcode"
path = os.path.join(model_root,"detect.prototxt")
path2 = os.path.join(model_root,"detect.caffemodel")
path3 = os.path.join(model_root,"sr.prototxt")
path4 = os.path.join(model_root,"sr.caffemodel")
detector = cv2.wechat_qrcode_WeChatQRCode(path,path2,path3,path4)

if __name__ == '__main__':
    # Load image.
    if len(sys.argv) > 1:
        img = cv2.imread(sys.argv[1])
    else:
        img = cv2.imread('test.jpg')

    t1 = time.time()
    # Detect and decode.
    res, points = detector.detectAndDecode(img)
    t2 = time.time()
    # Detected outputs.
    if len(res) > 0:
        print('Time Taken : ', round(1000 * (t2 - t1), 1), ' ms')
        print('Output : ', res[0])
        print('Bounding Box : ', points)
        displayBbox(img, points)
    else:
        print('QRCode not detected')

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

