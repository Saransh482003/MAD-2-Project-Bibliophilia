from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date


db = SQLAlchemy()

class Books(db.Model):
    book_id = db.Column(db.String, primary_key=True)
    book_name = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    author_id = db.Column(db.String, nullable=False)
    section_id = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False, default="Fiction")
    date_added = db.Column(db.DateTime, nullable=False, default = datetime.strftime(datetime.today(), "%d-%m-%Y"))

class Authors(db.Model):
    author_id = db.Column(db.String, primary_key=True)
    author_name = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    dob = db.Column(db.DateTime, nullable=False, default = datetime.strftime(date(1900,8,2), "%d-%m-%Y"))
    dod = db.Column(db.DateTime, nullable=True)
    country = db.Column(db.String, nullable=False)  
    avg_rating = db.Column(db.Float, nullable=False)

class Users(db.Model):
    user_id = db.Column(db.String, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    ph_no = db.Column(db.String, nullable=False)
    last_loged = db.Column(db.DateTime, default = datetime.strftime(date(2018,1,23), "%d-%m-%Y"))
    gender = db.Column(db.String, nullable=False)
    doj = db.Column(db.DateTime, default = datetime.strftime(date(2018,1,14), "%d-%m-%Y"), nullable=False)
    dob = db.Column(db.DateTime, default = datetime.strftime(date(1990,8,4), "%d-%m-%Y"), nullable=False)

class Sections(db.Model):
    section_id = db.Column(db.String, primary_key=True)
    section_name = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default = datetime.strftime(datetime.today(), "%d-%m-%Y"))

class Ratings(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)
    feedback = db.Column(db.String, nullable=False)
    __table_args__ = (db.UniqueConstraint('book_id', 'user_id', name='user_book_unique'),)
    
class Issues(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    request_date = db.Column(db.DateTime, nullable=False, default = datetime.strftime(datetime.today(), "%d-%m-%Y"))
    doi = db.Column(db.DateTime, nullable=False, default = datetime.strftime(datetime.today(), "%d-%m-%Y"))
    dor = db.Column(db.DateTime, nullable=False, default = datetime.strftime(datetime.today(), "%d-%m-%Y"))
    __table_args__ = (db.UniqueConstraint('book_id', 'user_id', name='user_book_unique'),)

class Requests(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    request_date = db.Column(db.DateTime, nullable=False, default = datetime.strftime(datetime.today(), "%d-%m-%Y"))
    __table_args__ = (db.UniqueConstraint('book_id', 'user_id', name='user_book_unique'),)