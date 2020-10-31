import uuid

from flask import Flask, render_template, redirect, url_for
from forms import SearchNewsClippingForm
from predictor import authenticity_predictor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_PROJECT'


@app.route('/', methods=['GET', 'POST'])
def display_homepage():
    news_clipping_form = SearchNewsClippingForm()
    return render_template('index.html', template_news_form=news_clipping_form, uuid=uuid.uuid1())


@app.route('/check-authenticity/<uuid>', methods=['POST'])
def check_authenticity(uuid):
    news_clipping_form = SearchNewsClippingForm()
    if news_clipping_form.validate_on_submit():
        url = news_clipping_form.url.data
        global prediction
        prediction = authenticity_predictor(url)
    return redirect(url_for('result', uuid=uuid, _external=True, _scheme='http'))

@app.route('/result/<uuid>/', methods=['GET'])
def result(uuid):
    return str(prediction)
