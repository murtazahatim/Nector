import pickle
import zipfile
import constant
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
from sklearn.tree import DecisionTreeClassifier
from storage_helper import file_exists


def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str


def train_model(fake_news_dataset, real_news_dataset):
    with zipfile.ZipFile(fake_news_dataset, 'r') as zip_ref:
        zip_ref.extractall(constant.DATASET_DIR)
    with zipfile.ZipFile(real_news_dataset, 'r') as zip_ref:
        zip_ref.extractall(constant.DATASET_DIR)
    fake = pd.read_csv(constant.DATASET_DIR + "Fake.csv")
    true = pd.read_csv(constant.DATASET_DIR + "True.csv")
    fake['target'] = 'fake'
    true['target'] = 'true'
    data = pd.concat([fake, true]).reset_index(drop=True)
    data = shuffle(data)
    data = data.reset_index(drop=True)
    data.drop(["date", "title"], axis=1, inplace=True)
    data['text'] = data['text'].apply(lambda x: x.lower())
    data['text'] = data['text'].apply(punctuation_removal)
    nltk.download('stopwords')
    stop = stopwords.words('english')
    data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))
    x = data['text']
    y = data.target
    pipe = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('model', DecisionTreeClassifier(criterion='entropy',
                                                      max_depth=20,
                                                      splitter='best',
                                                      random_state=42))])
    model = pipe.fit(x, y)
    finalized_model = constant.MODEL_DIR + constant.MODEL_NAME
    pickle.dump(model, open(finalized_model, 'wb'))


def predict_label(x, model_name):
    if not file_exists(constant.MODEL_DIR + model_name):
        train_model(constant.DATASET_DIR + 'Fake.csv.zip', constant.DATASET_DIR + 'True.csv.zip')
    prediction_model = load_model(constant.MODEL_NAME)
    x = pd.Series(x)
    x = (x.apply(lambda c: c.lower())).apply(punctuation_removal)
    x[0] = " ".join(x[0].split())
    nltk.download('stopwords')
    stop = stopwords.words('english')
    x = x.apply(lambda c: ' '.join([word for word in c.split() if word not in stop]))
    return prediction_model.predict(x)[0]


def load_model(model_name):
    finalized_model = constant.MODEL_DIR + model_name
    return pickle.load(open(finalized_model, 'rb'))