import os
import shutil

# Đường dẫn tới thư mục gốc của dự án
root_dir = os.getcwd()

# Duyệt tất cả các thư mục và tệp tin trong thư mục gốc của dự án
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Kiểm tra xem có thư mục __pycache__ trong danh sách thư mục không
    if '__pycache__' in dirnames:
        # Xóa toàn bộ thư mục __pycache__ và nội dung bên trong
        pycache_dir = os.path.join(dirpath, '__pycache__')
        print(f"Removing {pycache_dir}...")
        shutil.rmtree(pycache_dir)
