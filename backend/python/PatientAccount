import mysql.connector

class PatientAccount:
    def __init__(self, accountID, age, ssn, chart, insurancePolicy, bills):
        self.accountID = accountID
        self.age = age
        self.ssn = ssn
        self.chart = chart
        self.insurancePolicy = insurancePolicy
        self.bills = bills

class PatientAccountDatabase:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def add_patient_account(self, patient):
        query = "INSERT INTO patient_accounts (accountID, age, ssn, chart, insurancePolicy, bills) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (patient.accountID, patient.age, patient.ssn, patient.chart, patient.insurancePolicy, patient.bills)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_patient_account_by_id(self, accountID):
        query = "SELECT * FROM patient_accounts WHERE accountID = %s"
        self.cursor.execute(query, (accountID,))
        result = self.cursor.fetchone()
        if result:
            accountID, age, ssn, chart, insurancePolicy, bills = result
            return PatientAccount(accountID, age, ssn, chart, insurancePolicy, bills)
        else:
            return None

    def update_patient_account(self, patient):
        query = "UPDATE patient_accounts SET age=%s, ssn=%s, chart=%s, insurancePolicy=%s, bills=%s WHERE accountID=%s"
        values = (patient.age, patient.ssn, patient.chart, patient.insurancePolicy, patient.bills, patient.accountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_patient_account(self, accountID):
        query = "DELETE FROM patient_accounts WHERE accountID = %s"
        self.cursor.execute(query, (accountID,))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

# Example usage
if __name__ == "__main__":
    # Replace these values with your MySQL server credentials
    db = PatientAccountDatabase(host="localhost", user="your_username", password="your_password", database="MedPortal")

    # Add a new patient account
    new_patient = PatientAccount(accountID="123456", age=30, ssn="123-45-6789", chart="789012", insurancePolicy="456789", bills="789012")
    db.add_patient_account(new_patient)

    # Retrieve a patient account by ID
    retrieved_patient = db.get_patient_account_by_id("123456")
    if retrieved_patient:
        print("Retrieved patient:", retrieved_patient.accountID, retrieved_patient.age)
    else:
        print("Patient not found")

    # Update an existing patient account
    retrieved_patient.age = 35
    db.update_patient_account(retrieved_patient)

    # Delete a patient account
    db.delete_patient_account("123456")

    # Close the database connection
    db.close()
