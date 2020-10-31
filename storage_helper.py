import os
import shutil
import html2text
import constant
from urllib.request import urlopen


def download_webpage(uuid, url):
    webpage = urlopen(url)
    html_content = webpage.read()
    content_txt = html2text.html2text(html_content)
    file = open(constant.FILE_DIR + uuid + '.txt', 'w')
    file.write(content_txt)
    file.close()


def delete_directory(path):
    shutil.rmtree(path)


def file_exists(file_path):
    return os.path.exists(file_path)
