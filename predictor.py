import pickle
import constant
from sklearn.feature_extraction.text import TfidfVectorizer
from storage_helper import download_webpage, file_exists
from machine_learning_model.trainer import train_model


def authenticity_predictor(uuid, url):
    download_webpage(uuid, url)
    file = open(constant.FILE_DIR + uuid + '.txt')
    news_txt = file.read().replace("\n", " ")
    return predict(news_txt)


def predict(news_txt):

    if not file_exists(constant.MODEL_DIR + constant.MODEL_NAME):
        train_model(constant.DATASET_DIR + 'news.csv')
    prediction_model = load_model(constant.MODEL_NAME)

    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    tfidf_predict = tfidf_vectorizer.transform([news_txt])
    y_pred = prediction_model.predict(tfidf_predict)
    return True if y_pred[0] == 'REAL' else False


def load_model(model_name):
    finalized_model = constant.MODEL_DIR + model_name
    return pickle.load(open(finalized_model, 'rb'))