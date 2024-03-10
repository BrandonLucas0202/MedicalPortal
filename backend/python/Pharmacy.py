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

    # CRUD operations for Pharmacy
    def add_pharmacy(self, pharmacy):
        query = "INSERT INTO Pharmacy (pharmacyID, name, address, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (pharmacy.pharmacyID, pharmacy.name, pharmacy.address, pharmacy.phoneNumber)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_pharmacy_by_id(self, pharmacyID):
        query = "SELECT * FROM Pharmacy WHERE pharmacyID = %s"
        self.cursor.execute(query, (pharmacyID,))
        result = self.cursor.fetchone()
        if result:
            pharmacyID, name, address, phoneNumber = result
            return Pharmacy(pharmacyID, name, address, phoneNumber)
        else:
            return None

    def update_pharmacy(self, pharmacy):
        query = "UPDATE Pharmacy SET name=%s, address=%s, phoneNumber=%s WHERE pharmacyID=%s"
        values = (pharmacy.name, pharmacy.address, pharmacy.phoneNumber, pharmacy.pharmacyID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_pharmacy(self, pharmacyID):
        query = "DELETE FROM Pharmacy WHERE pharmacyID = %s"
        self.cursor.execute(query, (pharmacyID,))
        self.connection.commit()
