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

class AppointmentStatus(db.Model):
    __tablename__ = 'Appointment_Status'
    Id = db.Column(db.Integer, primary_key=True)
    StatusDescription = db.Column(db.String(50), nullable=False)

class Appointment(db.Model):
    __tablename__ = 'Appointments'
    Id = db.Column(db.Integer, primary_key=True)
    PatientID = db.Column(db.Integer, db.ForeignKey('Patients.Id'), nullable=False)
    DoctorID = db.Column(db.Integer, db.ForeignKey('Doctors.Id'), nullable=False)
    AppointmentDateTimeStart = db.Column(db.DateTime, nullable=False)
    AppointmentDateTimeEnd = db.Column(db.DateTime, nullable=False)
    StatusID = db.Column(db.Integer, db.ForeignKey('Appointment_Status.Id'), nullable=False)
    ReasonForVisit = db.Column(db.String(255), nullable=True)

    patient = db.relationship("Patient", backref="appointments")
    doctor = db.relationship("Doctor", backref="appointments")
    status = db.relationship("AppointmentStatus", backref="appointments")
