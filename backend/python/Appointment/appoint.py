# Import necessary libraries for database connection
import pymysql

# Create a function to establish database connection
def connect_to_database():
    db = pymysql.connect(
        host="15.204.226.232",
        user="student",
        password="goherd",
        database="MedPortal"
    )
    return db

# Function to insert a new appointment into the database
def insert_appointment(appointmentID, type, date, time, patientAccountID, doctorAccountID):
    db = connect_to_database()
    cursor = db.cursor()

    sql = "INSERT INTO Appointment (appointmentID, type, date, time, patientAccountID, doctorAccountID) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (appointmentID, type, date, time, patientAccountID, doctorAccountID)

    cursor.execute(sql, values)
    db.commit()

# Function to update an existing appointment in the database
def update_appointment(appointmentID, type, date, time, patientAccountID, doctorAccountID):
    db = connect_to_database()
    cursor = db.cursor()

    sql = "UPDATE Appointment SET type = %s, date = %s, time = %s, patientAccountID = %s, doctorAccountID = %s WHERE appointmentID = %s"
    values = (type, date, time, patientAccountID, doctorAccountID, appointmentID)

    cursor.execute(sql, values)
    db.commit()

# Function to delete an appointment from the database
def delete_appointment(appointmentID):
    db = connect_to_database()
    cursor = db.cursor()

    sql = "DELETE FROM Appointment WHERE appointmentID = %s"
    values = (appointmentID,)

    cursor.execute(sql, values)
    db.commit()

# Function to query an appointment from the database
def query_appointment(appointmentID):
    db = connect_to_database()
    cursor = db.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM Appointment WHERE appointmentID = %s"
    values = (appointmentID,)

    cursor.execute(sql, values)
    result = cursor.fetchone()

    return result

# Function to insert sample data into the database for testing
def insert_sample_data():
    insert_appointment('123456', 'Consultation', '2022-10-20', '09:00:00', 'patient123', 'doctor456')
    insert_appointment('789012', 'FollowUp', '2022-11-15', '14:30:00', 'patient789', 'doctor123')

# Call the function to insert sample data
insert_sample_data()
