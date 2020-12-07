from flask import render_template, request, redirect, url_for, flash
from . import main
import logging
from flask_login import current_user, login_user
from ..common import constants
from ..models.weather_model import Weather_model


@main.route('/')
def index():
    logging.info("index called")
    latest_readings = Weather_model.get_latest_readings()
    return render_template('index.html',latest_readings=latest_readings)


@main.route('/show_values',methods=['GET'])
def show_values():
    type_of_reader = request.args.get('select_reader',default='all')
    logging.info("GET request show_values?reader=%s" % type_of_reader)
    values = Weather_model.get_all(type_of_reader)
    return render_template('show_all.html',values = values)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)