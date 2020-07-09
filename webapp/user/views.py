from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Authorization'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['Post'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Successfull')
            return redirect(url_for('news.index'))
    flash('Not correct login or password')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash("Successful logout")
    return redirect(url_for('news.index'))


@blueprint.route('/registration')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Registration'
    login_form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=login_form)


@blueprint.route('/process-reg', methods=['Post'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        news_user = User(username=form.username.data, email=form.email.data, role='user')
        news_user.set_password(form.password.data)
        db.session.add(news_user)
        db.session.commit()
        flash('You successfully registrated')
        return redirect(url_for('user.login'))
    flash('Please input proper registration data')
    return redirect(url_for('user.register'))
