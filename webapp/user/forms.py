from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('User Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Remeber me', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Send', render_kw={'class': 'btn btn-primary'})


class RegistrationForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})
    password = PasswordField('User Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Remeber me', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Send', render_kw={'class': 'btn btn-primary'})
    