from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class SearchNewsClippingForm(FlaskForm):
    url = StringField('Article/News Clipping URL', validators=[DataRequired(), URL(message='Please enter a valid URL')])
    submit = SubmitField('Check Authenticity')
