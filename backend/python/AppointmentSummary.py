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

  # CRUD operations for AppointmentSummary
    def add_appointment_summary(self, appointment_summary):
        query = "INSERT INTO AppointmentSummary (appointmentSummaryID, doctorAccountID, appointmentID, patientID) VALUES (%s, %s, %s, %s)"
        values = (appointment_summary.appointmentSummaryID, appointment_summary.doctorAccountID, appointment_summary.appointmentID, appointment_summary.patientID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_appointment_summary_by_id(self, appointmentSummaryID):
        query = "SELECT * FROM AppointmentSummary WHERE appointmentSummaryID = %s"
        self.cursor.execute(query, (appointmentSummaryID,))
        result = self.cursor.fetchone()
        if result:
            appointmentSummaryID, doctorAccountID, appointmentID, patientID = result
            return AppointmentSummary(appointmentSummaryID, doctorAccountID, appointmentID, patientID)
        else:
            return None

    def update_appointment_summary(self, appointment_summary):
        query = "UPDATE AppointmentSummary SET doctorAccountID=%s, appointmentID=%s, patientID=%s WHERE appointmentSummaryID=%s"
        values = (appointment_summary.doctorAccountID, appointment_summary.appointmentID, appointment_summary.patientID, appointment_summary.appointmentSummaryID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_appointment_summary(self, appointmentSummaryID):
        query = "DELETE FROM AppointmentSummary WHERE appointmentSummaryID = %s"
        self.cursor.execute(query, (appointmentSummaryID,))
        self.connection.commit()
