from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import os
import numpy as np
def ocr(img_path):
    ocr_ins = PaddleOCR(use_angle_cls=True, lang="ch",use_gpu=True,det_model_dir='./models/det/ch_PP-OCRv4_det_server_infer',rec_model_dir='./models/rec/ch/ch_PP-OCRv4_rec_infer',cls_model_dir='./models/cls/ch_ppocr_mobile_v2.0_cls_infer')

    result = ocr_ins.ocr(img_path, cls=True)

    return result
    #showresult(result,img_path)

if __name__ == '__main__':
    folder_path = './result/temp/'
    files = os.listdir(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in files]
    for t in file_paths:
        print(ocr(t))
    