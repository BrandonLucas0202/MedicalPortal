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

# CRUD operations for Doctor
    def add_doctor(self, doctor):
        query = "INSERT INTO Doctor (doctorID, staffAccountID) VALUES (%s, %s)"
        values = (doctor.doctorID, doctor.staffAccountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_doctor_by_id(self, doctorID):
        query = "SELECT * FROM Doctor WHERE doctorID = %s"
        self.cursor.execute(query, (doctorID,))
        result = self.cursor.fetchone()
        if result:
            doctorID, staffAccountID = result
            return Doctor(doctorID, staffAccountID)
        else:
            return None

    def update_doctor(self, doctor):
        query = "UPDATE Doctor SET staffAccountID = %s WHERE doctorID = %s"
        values = (doctor.staffAccountID, doctor.doctorID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_doctor(self, doctorID):
        query = "DELETE FROM Doctor WHERE doctorID = %s"
        self.cursor.execute(query, (doctorID,))
        self.connection.commit()
