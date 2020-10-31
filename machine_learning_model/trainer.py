"""
Credits: Dataflair (https://data-flair.training)
"""

import pandas as pd
import pickle
import constant
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier


def train_model(dataset):
    #Read the data
    df = pd.read_csv(dataset)

    #Get shape and head
    df.shape
    df.head()

    #Get the labels
    labels = df.label
    labels.head()

    x = df['text']
    y = labels

    tfidf_train = fit_transform_vectorizer(x)

    #Initialize a PassiveAggressiveClassifier
    pac = PassiveAggressiveClassifier(max_iter=50)
    pac.fit(tfidf_train, y)

    finalized_model = constant.MODEL_DIR + constant.MODEL_NAME
    pickle.dump(pac, open(finalized_model, 'wb'))


def fit_transform_vectorizer(x_train, x_test=None):
    # Initialize a TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    # Fit and transform train set, transform test set
    tfidf_train = tfidf_vectorizer.fit_transform(x_train)

    if x_test is not None:
        tfidf_test = tfidf_vectorizer.transform(x_test)
        return tfidf_train, tfidf_test
    else:
        return tfidf_train