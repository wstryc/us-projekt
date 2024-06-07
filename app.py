from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Define the Doctor model
class Doctor(db.Model):
    __tablename__ = 'Doctors'
    Id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Specialty = db.Column(db.String(100))
    PhoneNumber = db.Column(db.String(15))
    Email = db.Column(db.String(100))

# Landing page
@app.route('/')
def introduction():
    return render_template('introduction.html')
# Doctors page
@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)

# Run the Flask application
if __name__ == '__main__':
    app.debug = True
    app.run()
