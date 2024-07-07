
import numpy as np
import os
from paddleocr import PaddleOCR
import re


def cluster(data):
    def gaussian_kernel(x, center, bandwidth):
        return np.exp(-0.5 * ((x - center) / bandwidth) ** 2) / (np.sqrt(2 * np.pi) * bandwidth)
    def mean_shift(data, bandwidth=1.0, max_iterations=100, convergence_threshold=1e-5):
        n_points = len(data)
        old_centers = np.copy(data)

        for _ in range(max_iterations):
            new_centers = np.zeros_like(data)

            for i in range(n_points):
                weights = gaussian_kernel(data[i], old_centers, bandwidth)
                new_centers[i] = int(np.sum(weights * old_centers) / np.sum(weights))

            # Check for convergence
            if np.linalg.norm(new_centers - old_centers) < convergence_threshold:
                break

            old_centers = new_centers
        # 标记簇
        labels = np.argmin(np.abs(data[:, None] - new_centers), axis=1)
        # 返回原始数据和所属簇
        result = np.column_stack(labels)
        return result
    # 使用Mean Shift算法进行聚类
    cluster_centers = mean_shift(data, bandwidth=5)
    return cluster_centers

def process(file_paths):
        ocr_ins = PaddleOCR(use_angle_cls=True, lang="ch",use_gpu=True,
                            det_model_dir='./models/det/ch_PP-OCRv4_det_server_infer',
                            rec_model_dir='./models/rec/ch/ch_PP-OCRv4_rec_server_infer',
                            cls_model_dir='./models/cls/ch_ppocr_mobile_v2.0_cls_infer')
        for file_path in file_paths:
            result = ocr_ins.ocr(file_path, cls=True)[0]
            # 数据处理
            num_results = len(result)
            x, y= np.zeros(num_results), np.zeros(num_results)
            label = []
            for idx, line in enumerate(result):
                x[idx], y[idx] = ((line[0][2][0] + line[0][0][0]) / 2,  # Midpoint x
                                  (line[0][0][1] + line[0][2][1]) / 2)  # Midpoint y
                label.append(line[1][0])

            c =cluster(y)
            unique_elements, counts = np.unique(c, return_counts=True)
            for i in range(len(unique_elements)):

                a = unique_elements[i]
                b = counts[i]
                if b<=1 or i==0:
                    continue
                sorted_indices = np.argsort(x[a:a + b])
                # 从一行的最后的字符串中找到数字,应该找单个数字
                numbers = re.findall(r'\d+', label[sorted_indices[-1] + a])
                # 将最后的字符串变为空格+纯数字
                label[sorted_indices[-1] + a] = ''.join(numbers)
                # 打开文件以供读取
                file_path = './result/txt/dic.txt'
                with open(file_path, 'a', encoding='utf-8') as file:
                    for j in range(b):
                        file.write(label[sorted_indices[j] + a])
                        file.write(' ')
                    file.write('\n')

if __name__ == '__main__':
    folder_path = './result/contents/'
    files = os.listdir(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in files]
    process(file_paths)








