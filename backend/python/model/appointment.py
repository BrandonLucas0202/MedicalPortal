"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Database Appointment object and Reminder object.
"""
from model.model import Model

class Appointment(Model):
    def __init__(self, appointmentID) -> None:
        Model.__init__(self, "Appointment", [
           "appointmentID", "description", "date", "time", "patientAccountID", "doctorAccountID"
        ], {"appointmentID": appointmentID})
        self.__appointmentID = appointmentID

    def getAppointmentID(self):
        return self.__appointmentID
    
class Reminder(Model):
    def __init__(self, reminderID) -> None:
        Model.__init__(self, "Reminder", [
           "reminderID", "description", "date", "time", "accountID"
        ], {"reminderID": reminderID})
        self.__reminderID = reminderID

    def getReminderID(self):
        return self.__reminderID