from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy db instance
db = SQLAlchemy()

# Define the Doctor model
class Doctor(db.Model):
    __tablename__ = 'Doctors'
    Id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Specialty = db.Column(db.String(100))
    PhoneNumber = db.Column(db.String(15))
    Email = db.Column(db.String(100))

class Patient(db.Model):
    __tablename__ = 'Patients'
    Id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    DateOfBirth = db.Column(db.Date)
    Gender = db.Column(db.String(10))
    PhoneNumber = db.Column(db.String(15))
    Email = db.Column(db.String(100))
    Address = db.Column(db.String(255))