from . import dashboard
from flask import render_template,request,g
import datetime as dt
import logging
from ...common import constants
from ...models.weather_model import Weather_model

@dashboard.route('/show_dashboard')
def show_dashboard():
    return render_template('dashboard.html')

@dashboard.route('/analyse')
def analyse():
    day_ago = dt.datetime.utcnow() - dt.timedelta(days=1)
    readers = [constants.DHT11_temp,constants.DHT11_humidity]
    values = {}
    for reader in readers:
        values[reader] = (Weather_model.get_values_by_date(day_ago,reader))
    return render_template('dashboard.html',readings=values)