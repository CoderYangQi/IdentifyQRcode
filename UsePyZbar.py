import cv2
from pyzbar.pyzbar import decode


def mainZbar():
    img = cv2.imread("test.jpg")

    decoded_objs = decode(img)
    for obj in decoded_objs:
        print("data is : ",obj.data.decode())

if __name__ == '__main__':
    mainZbar()

