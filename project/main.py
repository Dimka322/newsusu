from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from . import db
from .models import Film

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        result = Film.query.filter_by(name=form.name.data).first()
        # flash(result.name)
        if form.name.data.lower() == 'First Film'.lower():
            return redirect(url_for('main.film'))
        elif form.name.data.lower() == 'Second Film'.lower():
            return redirect(url_for('main.second_film'))
        elif form.name.data.lower() == 'Third Film'.lower():
            return redirect(url_for('main.third_film'))
        elif form.name.data.lower() == 'Fourth Film'.lower():
            return redirect(url_for('main.four_film'))
    return render_template("index.html", form=form)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/firstfilm')
def film():

    return render_template('film.html')


@main.route('/secondfilm')
def second_film():
    return render_template('secondfilm.html')


@main.route('/thirdfilm')
def third_film():
    return render_template('thirdfilm.html')


@main.route('/fourthfilm')
def four_film():
    return render_template('fourthfilm.html')


@main.route('/faq')
def faq():
    return render_template('faq.html')


class SearchForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
