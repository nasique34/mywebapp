from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Arrival, Nationality

@app.route('/')
@app.route('/index')
def index():
    arrivals = Arrival.query.all()
    return render_template('index.html', arrivals=arrivals)

from datetime import datetime

@app.route('/add', methods=['GET', 'POST'])
def add():
    nationalities = Nationality.query.all()
    if request.method == 'POST':
        birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d').date()
        arrival_date = datetime.strptime(request.form['arrival_date'], '%Y-%m-%d').date()
        departure_date = datetime.strptime(request.form['departure_date'], '%Y-%m-%d').date()
        arrival = Arrival(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            birth_date=birth_date,
            nationality_id=request.form['nationality_id'],
            arrival_date=arrival_date,
            departure_date=departure_date
        )
        db.session.add(arrival)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', nationalities=nationalities)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    nationalities = Nationality.query.all()
    arrival = Arrival.query.get(id)
    if request.method == 'POST':
        arrival.first_name = request.form['first_name']
        arrival.last_name = request.form['last_name']
        arrival.birth_date = request.form['birth_date']
        arrival.nationality_id = request.form['nationality_id']
        arrival.arrival_date = request.form['arrival_date']
        arrival.departure_date = request.form['departure_date']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', arrival=arrival, nationalities=nationalities)

@app.route('/add_nationality', methods=['GET', 'POST'])
def add_nationality():
    if request.method == 'POST':
        nationality = Nationality(name=request.form['name'])
        db.session.add(nationality)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_nationality.html')
