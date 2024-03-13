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

  # CRUD operations for AppointmentReminder
    def add_appointment_reminder(self, appointment_reminder):
        query = "INSERT INTO AppointmentReminder (appointmentReminderID, appointmentID, reminderID) VALUES (%s, %s, %s)"
        values = (appointment_reminder.appointmentReminderID, appointment_reminder.appointmentID, appointment_reminder.reminderID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_appointment_reminder_by_id(self, appointmentReminderID):
        query = "SELECT * FROM AppointmentReminder WHERE appointmentReminderID = %s"
        self.cursor.execute(query, (appointmentReminderID,))
        result = self.cursor.fetchone()
        if result:
            appointmentReminderID, appointmentID, reminderID = result
            return AppointmentReminder(appointmentReminderID, appointmentID, reminderID)
        else:
            return None

    def update_appointment_reminder(self, appointment_reminder):
        query = "UPDATE AppointmentReminder SET appointmentID=%s, reminderID=%s WHERE appointmentReminderID=%s"
        values = (appointment_reminder.appointmentID, appointment_reminder.reminderID, appointment_reminder.appointmentReminderID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_appointment_reminder(self, appointmentReminderID):
        query = "DELETE FROM AppointmentReminder WHERE appointmentReminderID = %s"
        self.cursor.execute(query, (appointmentReminderID,))
        self.connection.commit()
