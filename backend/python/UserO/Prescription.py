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

    # Other methods...

    # CRUD operations for Prescription
    def add_prescription(self, prescription):
        query = "INSERT INTO Prescription (prescriptionID, drug, dosage, frequency, date, pharmacyID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (prescription.prescriptionID, prescription.drug, prescription.dosage, prescription.frequency, prescription.date, prescription.pharmacyID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_prescription_by_id(self, prescriptionID):
        query = "SELECT * FROM Prescription WHERE prescriptionID = %s"
        self.cursor.execute(query, (prescriptionID,))
        result = self.cursor.fetchone()
        if result:
            prescriptionID, drug, dosage, frequency, date, pharmacyID = result
            return Prescription(prescriptionID, drug, dosage, frequency, date, pharmacyID)
        else:
            return None

    def update_prescription(self, prescription):
        query = "UPDATE Prescription SET drug=%s, dosage=%s, frequency=%s, date=%s, pharmacyID=%s WHERE prescriptionID=%s"
        values = (prescription.drug, prescription.dosage, prescription.frequency, prescription.date, prescription.pharmacyID, prescription.prescriptionID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_prescription(self, prescriptionID):
        query = "DELETE FROM Prescription WHERE prescriptionID = %s"
        self.cursor.execute(query, (prescriptionID,))
        self.connection.commit()

    # Other methods...

# Example usage
if __name__ == "__main__":
    # Replace these values with your MySQL server credentials
    db = PatientAccountDatabase(host="localhost", user="your_username", password="your_password", database="MedPortal")

    # Example operations
    # Add a new prescription
    new_prescription = Prescription(prescriptionID="789", drug="MedicineX", dosage="10mg", frequency="Once daily", date="2024-03-09", pharmacyID="123456")
    db.add_prescription(new_prescription)

    # Retrieve a prescription by ID
    retrieved_prescription = db.get_prescription_by_id("789")
    if retrieved_prescription:
        print("Retrieved prescription:", retrieved_prescription.prescriptionID, retrieved_prescription.drug)
    else:
        print("Prescription not found")

    # Close the database connection
    db.close()
