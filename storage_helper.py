import os
import subprocess
import shutil
import constant


def download_webpage(url):
    subprocess.run(['clean-mark', url, '-t', 'text'], cwd=constant.FILE_DIR)


def delete_directory(path):
    shutil.rmtree(path)


def file_exists(file_path):
    return os.path.exists(file_path)
