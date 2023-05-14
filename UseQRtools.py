import qrcode
# from qrtools.qrtools import QR

from qreader import QReader
import cv2


def main():
    ImgPath = r"test.jpg"
    # qr = QR()
    # qr.decode(ImgPath)
    # print("QRtools result is : ",qr.data)

    qreader = QReader()
    img = cv2.imread(ImgPath)
    text = qreader.detect_and_decode(image=img)
    print(text)





if __name__ == '__main__':
    main()
