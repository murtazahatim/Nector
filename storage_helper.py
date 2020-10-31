import os
import shutil
from newspaper import Article
import constant


def download_webpage(uuid, url):
    article = Article(url)
    article.download()
    file = open(constant.FILE_DIR + uuid + '.txt', 'w')
    file.write(article.text)
    file.close()


def delete_directory(path):
    shutil.rmtree(path)


def file_exists(file_path):
    return os.path.exists(file_path)
