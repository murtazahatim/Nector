import pickle
import constant
import pandas as pd
import os
from storage_helper import download_webpage, file_exists
from machine_learning_model.trainer import train_model, fit_transform_vectorizer


def authenticity_predictor(url):
    download_webpage(url)
    news_lines = []
    with open(constant.FILE_DIR + os.listdir(constant.FILE_DIR)[0]) as text_file:
        for line in text_file:
            news_lines.append(line)

    news_txt = ' '.join(news_lines[10:]).replace("\n", " ")
    print(news_txt)
    return predict(news_txt)


def predict(news_txt):

    if not file_exists(constant.MODEL_DIR + constant.MODEL_NAME):
        train_model(constant.DATASET_DIR + 'news.csv')
    prediction_model = load_model(constant.MODEL_NAME)

    df = pd.read_csv(constant.DATASET_DIR + 'news.csv')
    x_dataset = df['text']
    tfidf_predict = fit_transform_vectorizer(x_dataset, [news_txt])[1]
    y_pred = prediction_model.predict(tfidf_predict)
    print(y_pred)
    return True if y_pred[0] == 'REAL' else False


def load_model(model_name):
    finalized_model = constant.MODEL_DIR + model_name
    return pickle.load(open(finalized_model, 'rb'))