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

    # CRUD operations for Laboratory
    def add_laboratory(self, laboratory):
        query = "INSERT INTO Laboratory (labID, name, address, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (laboratory.labID, laboratory.name, laboratory.address, laboratory.phoneNumber)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_laboratory_by_id(self, labID):
        query = "SELECT * FROM Laboratory WHERE labID = %s"
        self.cursor.execute(query, (labID,))
        result = self.cursor.fetchone()
        if result:
            labID, name, address, phoneNumber = result
            return Laboratory(labID, name, address, phoneNumber)
        else:
            return None

    def update_laboratory(self, laboratory):
        query = "UPDATE Laboratory SET name=%s, address=%s, phoneNumber=%s WHERE labID=%s"
        values = (laboratory.name, laboratory.address, laboratory.phoneNumber, laboratory.labID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_laboratory(self, labID):
        query = "DELETE FROM Laboratory WHERE labID = %s"
        self.cursor.execute(query, (labID,))
        self.connection.commit()
