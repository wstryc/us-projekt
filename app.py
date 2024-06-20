from flask import Flask, render_template, request, redirect, url_for
from models import db, Doctor, Patient, Appointment, AppointmentStatus
from datetime import datetime


# Initialize app
app = Flask(__name__)

# Define variables
DB_USERNAME='us-project-server-admin'
DB_PASSWORD='this!is!pwd123'
DB_NAME='us-project-database'
DB_SERVER='us-project-server.database.windows.net'

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+18+for+SQL+Server'
    .format(
        username=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_NAME,
        server=DB_SERVER
    )
)

# Intialize DB connection
db.init_app(app)

# Landing page
@app.route('/')
def introduction():
    return render_template('introduction.html')

# Doctors page
@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)

@app.route('/register_patient', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d')
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        email = request.form['email']
        address = request.form['address']
        
        new_patient = Patient(
            FirstName=first_name,
            LastName=last_name,
            DateOfBirth=date_of_birth,
            Gender=gender,
            PhoneNumber=phone_number,
            Email=email,
            Address=address
        )
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('list_patients'))
    return render_template('register_patient.html')

# Define a route for the list of patients
@app.route('/patients')
def list_patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

# Define a route to delete a patient
@app.route('/delete_patient/<int:patient_id>')
def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('list_patients'))

# Define a route to update a patient
@app.route('/update_patient/<int:patient_id>', methods=['GET', 'POST'])
def update_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return "Patient not found", 404
    if request.method == 'POST':
        patient.FirstName = request.form['first_name']
        patient.LastName = request.form['last_name']
        patient.DateOfBirth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d')
        patient.Gender = request.form['gender']
        patient.PhoneNumber = request.form['phone_number']
        patient.Email = request.form['email']
        patient.Address = request.form['address']
        
        db.session.commit()
        return redirect(url_for('list_patients'))
    return render_template('update_patient.html', patient=patient)

# Define a route to register a new appointment
@app.route('/register_appointment', methods=['GET', 'POST'])
def register_appointment():
    patients = Patient.query.all()
    doctors = Doctor.query.all()
    statuses = AppointmentStatus.query.all()
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        appointment_start = datetime.strptime(request.form['appointment_start'], '%Y-%m-%dT%H:%M')
        appointment_end = datetime.strptime(request.form['appointment_end'], '%Y-%m-%dT%H:%M')
        status_id = request.form['status_id']
        reason = request.form['reason']
        
        new_appointment = Appointment(
            PatientID=patient_id,
            DoctorID=doctor_id,
            AppointmentDateTimeStart=appointment_start,
            AppointmentDateTimeEnd=appointment_end,
            StatusID=status_id,
            ReasonForVisit=reason
        )
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('list_appointments'))
    return render_template('register_appointment.html', patients=patients, doctors=doctors, statuses=statuses)

# Define a route for the list of appointments
@app.route('/appointments')
def list_appointments():
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

# Define a route to delete an appointment
@app.route('/delete_appointment/<int:appointment_id>')
def delete_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    db.session.delete(appointment)
    db.session.commit()
    return redirect(url_for('list_appointments'))

# Run the Flask application
if __name__ == '__main__':
    app.debug = True
    app.run()
