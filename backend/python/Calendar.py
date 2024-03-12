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

    # CRUD operations for Calendar
    def add_calendar(self, calendar):
        query = "INSERT INTO Calendar (calendarID) VALUES (%s)"
        values = (calendar.calendarID,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_calendar_by_id(self, calendarID):
        query = "SELECT * FROM Calendar WHERE calendarID = %s"
        self.cursor.execute(query, (calendarID,))
        result = self.cursor.fetchone()
        if result:
            calendarID = result[0]
            return Calendar(calendarID)
        else:
            return None

    def update_calendar(self, calendar):
        query = "UPDATE Calendar SET calendarID = %s WHERE calendarID = %s"
        values = (calendar.calendarID, calendar.calendarID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_calendar(self, calendarID):
        query = "DELETE FROM Calendar WHERE calendarID = %s"
        self.cursor.execute(query, (calendarID,))
        self.connection.commit()
