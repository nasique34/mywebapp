from app import db

class Arrival(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    nationality_id = db.Column(db.Integer, db.ForeignKey('nationality.id'))
    arrival_date = db.Column(db.Date, nullable=False)
    departure_date = db.Column(db.Date)

    nationality = db.relationship('Nationality', backref='arrivals')

    # Add any other fields and methods here
