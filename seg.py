import fitz
import os
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from paddleocr import PaddleOCR
def extract_images(pdf_file_path=str,start=0,end=0):#提取页面
    doc = fitz.open(pdf_file_path)
    out_path='./result/contents/'
    print(pdf_file_path)

    for i in range(start-1,end):
        page = doc.load_page(i)
        mat = fitz.Matrix(2,2)  # zoom factor 2 in each dimension'
        pix=page.get_pixmap(matrix=mat, alpha=False)
        if pix.width < 3000 or pix.height < 3000:
            pix = page.get_pixmap(matrix=fitz.Matrix(4,4), alpha=False)
        if pix.width < 3000 or pix.height < 3000:
            pix = page.get_pixmap(matrix=fitz.Matrix(8,8), alpha=False)
        image_path = os.path.join(out_path, "{:0>4}.png".format(page.number))
        pix.save(image_path)

    doc.close()

def half(folder_path = './result/contents/'):#对双栏目录进行切割
    path_list = os.listdir(folder_path)
    ocr_ins = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True,
                        det_model_dir='./models/det/ch_PP-OCRv4_det_server_infer',
                        rec_model_dir='./models/rec/ch/ch_PP-OCRv4_rec_infer',
                        cls_model_dir='./models/cls/ch_ppocr_mobile_v2.0_cls_infer')
    for i in path_list:
        dir_image = os.path.join(folder_path, i)
        result = ocr_ins.ocr(dir_image, cls=True)[0]
        # 数据处理
        num_results = len(result)
        x, y  = np.zeros(num_results), np.zeros(num_results)
        q, h =  np.zeros(num_results), np.zeros(num_results)
        label = []
        for idx, line in enumerate(result):
            x[idx], y[idx] = ((line[0][2][0] + line[0][0][0]) / 2,  # Midpoint x
                              (line[0][0][1] + line[0][2][1]) / 2)  # Midpoint y
            q[idx], h[idx] = line[0][0][0], line[0][2][0]  # Start x, End x
            label.append(line[1][0])

        data_2d = np.zeros((x.shape[0], 2))
        data_2d[:, 0] = x
        kmeans = KMeans(n_clusters=4, random_state=0).fit(data_2d)
        cluster = []
        cluster.append(x[kmeans.labels_ == 0])
        cluster.append(x[kmeans.labels_ == 1])
        cluster.append(x[kmeans.labels_ == 2])
        cluster.append(x[kmeans.labels_ == 3])
        m = np.zeros(4)
        m[0],m[1] = np.mean(cluster[0]),np.mean(cluster[1])
        m[2],m[3] = np.mean(cluster[2]),np.mean(cluster[3])
        # 找到最大值和最小值的索引
        max_index = np.argmax(m)
        min_index = np.argmin(m)
        t = []  # 中间两值的索引
        for e in range(4):
            if e != max_index:
                if e != min_index:
                    t.append(int(e))
        o = []
        if (m[t[0]] < m[t[1]]):
            o.append(h[kmeans.labels_ == t[0]])
            o.append(q[kmeans.labels_ == t[1]])
        else:
            o.append(h[kmeans.labels_ == t[1]])
            o.append(q[kmeans.labels_ == t[0]])
        c2 = np.mean(o[0])
        c3 = np.mean(o[1])
        a = open(os.path.join(folder_path, i), 'rb')
        img = Image.open(a)
        w = img.width  # 图片的宽
        h = img.height  # 图片的高
        # box元组内分别是 所处理图片中想要截取的部分的 左上角和右下角的坐标
        box = (0,0,int((c2+c3)/2),h)
        img_left = img.crop(box)
        image_path = os.path.join(folder_path, i+"_1.png")
        # 这里需要对截出的图加一个字母进行标识，防止名称相同导致覆盖
        img_left.save(image_path)
        box = (int((c2 + c3) / 2), 0, w, h)
        img_right = img.crop(box)
        image_path = os.path.join(folder_path, i + "_2.png")
        img_right.save(image_path)
        a.close()
    for i in path_list:#删除原来的图像
        os.remove(os.path.join(folder_path, i))

if __name__ == '__main__':
    extract_images("C:/Code/计算机视觉教程.pdf",7,10)
    folder_path = './result/contents/'
    half(folder_path)




