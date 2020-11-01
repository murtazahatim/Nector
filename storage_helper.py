import os
import subprocess
import shutil
import constant


def download_webpage(uuid, url):
    if not file_exists(constant.FILE_DIR):
        os.mkdir(constant.FILE_DIR)

    if not file_exists(constant.FILE_DIR + uuid):
        os.mkdir(constant.FILE_DIR + uuid)

    subprocess.run([constant.CLEAN_MARK_PATH, url, '-t', 'text'], cwd=constant.FILE_DIR + uuid)


def delete_files(files):
    for file in files:
        if file_exists(file):
            os.remove(file)


def delete_directory(path):
    shutil.rmtree(path)


def file_exists(file_path):
    return os.path.exists(file_path)
