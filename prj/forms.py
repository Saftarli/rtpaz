from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField( validators=[DataRequired(),Length(min=2,max=30)])
    email = StringField('Email', validators=[DataRequired(),Email(),Length(max=60)])
    subject = StringField('Subject', validators=[DataRequired(),Length(max=10)])
    message = TextAreaField('Message',validators=[DataRequired(),Length(min=10,max=500)])