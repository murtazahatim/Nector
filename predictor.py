import constant
import os
from storage_helper import download_webpage, delete_directory, delete_files
from machine_learning_model.trainer import predict_label


def authenticity_predictor(uuid, url):
    download_webpage(uuid, url)
    news_lines = []
    with open(constant.FILE_DIR + uuid + '/' + os.listdir(constant.FILE_DIR + uuid)[0]) as text_file:
        for line in text_file:
            news_lines.append(line)

    news_txt = ' '.join(news_lines[10:])
    print(news_txt)
    return predict(news_txt)


def predict(news_txt):
    result = predict_label([news_txt], constant.MODEL_NAME)
    cleanup_storage()
    return False if result == 'FAKE' else True


def cleanup_storage():
    delete_directory(constant.FILE_DIR)
    delete_files([constant.DATASET_DIR + 'Fake.csv', constant.DATASET_DIR + 'True.csv'])
