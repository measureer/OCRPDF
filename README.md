# OCRPDF
对PDF电子书籍目录页使用OCR技术提取文字信息，自动生成PDF书籍目录索引
#conda create -n ppocrlabel python=3.10.13
conda install paddlepaddle-gpu==2.6.0 cudatoolkit=11.7 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge
pip install "paddleocr>=2.0.1" 
pip install pyside6 -i https://mirror.baidu.com/pypi/simple
pip install PySide6-Fluent-Widgets -i https://pypi.org/simple/
