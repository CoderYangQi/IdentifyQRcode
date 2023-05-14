from pyzxing import BarCodeReader
'''     
    #todo
    使用 zxing 识别 二维码
    
'''

def MainZxing():
    # img_path = r"test.jpg"
    img_path = "test1.jpg"
    reader = BarCodeReader()
    barcode = reader.decode(img_path)
    print("Zxing result is : ",barcode)




if __name__ == '__main__':
    MainZxing()

