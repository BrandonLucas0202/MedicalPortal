import mysql.connector

class PatientAccountDatabase:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

# CRUD operations for Appointment
    def add_appointment(self, appointment):
        query = "INSERT INTO Appointment (appointmentID, doctorID, patientID, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (appointment.appointmentID, appointment.doctorID, appointment.patientID, appointment.date, appointment.time, appointment.status)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_appointment_by_id(self, appointmentID):
        query = "SELECT * FROM Appointment WHERE appointmentID = %s"
        self.cursor.execute(query, (appointmentID,))
        result = self.cursor.fetchone()
        if result:
            appointmentID, doctorID, patientID, date, time, status = result
            return Appointment(appointmentID, doctorID, patientID, date, time, status)
        else:
            return None

    def update_appointment(self, appointment):
        query = "UPDATE Appointment SET doctorID=%s, patientID=%s, date=%s, time=%s, status=%s WHERE appointmentID=%s"
        values = (appointment.doctorID, appointment.patientID, appointment.date, appointment.time, appointment.status, appointment.appointmentID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_appointment(self, appointmentID):
        query = "DELETE FROM Appointment WHERE appointmentID = %s"
        self.cursor.execute(query, (appointmentID,))
        self.connection.commit()
