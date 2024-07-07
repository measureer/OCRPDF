import os
def clear(folder_path):
    try:
        # 获取文件夹中的所有文件和子文件夹
        files = os.listdir(folder_path)

        # 遍历文件夹中的每个文件
        for file in files:
            # 构建文件的完整路径
            file_path = os.path.join(folder_path, file)

            # 检查是否为文件，而不是子文件夹
            if os.path.isfile(file_path):
                # 删除文件
                os.remove(file_path)

        print(f"All files in {folder_path} have been cleared.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
if __name__ == '__main__':
   print("clear")