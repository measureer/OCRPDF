import sys
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QRadioButton,QFileDialog,QMessageBox
from Ui_demo import Ui_Form
import seg
import analysis
import bookmark
import clear
import os

class window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.out_path ='./result/out/'
        self.bind()
        self.setAcceptDrops(True)
        self.setFixedSize(867, 596)



    def dragEnterEvent(self, event):
        # 获取文件路径
        file = event.mimeData().urls()[0].toLocalFile()
        
        self.lineEdit_5.clear()  # 清空 lineEdit_5 的内容
        print("拖拽的文件 ==> {}".format(file))
        new_path = file.replace("/", "\\")
        self.lineEdit_5.setText(new_path)
        event.accept()

    def bind(self):
        self.pushButton.clicked.connect(self.get_file_path)
        self.pushButton_2.clicked.connect(self.seg)
        self.pushButton_3.clicked.connect(self.ocr)
        self.pushButton_4.clicked.connect(self.write)
        self.pushButton_5.clicked.connect(self.clear)
        self.pushButton_6.clicked.connect(self.one_click_completion)
        self.pushButton_7.clicked.connect(self.close)
        self.pushButton_8.clicked.connect(self.get_out_path)

    def get_file_path(self):
        file_dialog = QFileDialog()
        self.pdf_file_path, _ = file_dialog.getOpenFileName(self, "Open file", "", "PDF Files (*.pdf)")
        self.lineEdit_5.setText(self.pdf_file_path)

    def get_out_path(self):
        file_dialog = QFileDialog()
        self.out_path = file_dialog.getExistingDirectory(self, "Open file", "")
        self.lineEdit_4.setText(self.out_path)     
    
    def seg(self):
        start_page = self.lineEdit.text()
        end_page =self.lineEdit_2.text()
        offset = self.lineEdit_3.text()
        pdf_file_path=self.lineEdit_5.text()
        
        # Check if start_page and end_page are valid integers
        #print(pdf_file_path)
        try:
            start_page = int(start_page)
            end_page = int(end_page)
        except ValueError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please enter valid page numbers.")
            msg_box.exec_()
            return

        # 分割PDF
        seg.extract_images(pdf_file_path, start_page, end_page)
        folder_path = './result/contents/'
        double_bar = self.radioButton_2.isChecked()
        if double_bar:
            seg.half(folder_path)

    def ocr(self):
        # 获取目录图片路径
        folder_path = './result/contents/'
        files = os.listdir(folder_path)
        file_paths = [os.path.join(folder_path, file) for file in files]

        # 进行识别分析
        analysis.process(file_paths)
        
        
    def write(self):#写入书签
        file_path = './result/txt/dic.txt'
        offset = self.lineEdit_3.text()
        pdf_file_path=self.lineEdit_5.text()
        try:
            offset =int(offset)-1
        except ValueError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please enter valid page numbers.")
            msg_box.exec_()
            return

        bookmark.add_toc_from_file(file_path, pdf_file_path, offset, self.out_path + '/')

    def clear(self):
        contents_folder_path = "./result/contents"
        clear.clear(contents_folder_path)

        txt_folder_path = "./result/txt"
        clear.clear(txt_folder_path)

    def one_click_completion(self):
        self.seg()
        self.ocr()
        self.write()
        self.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())