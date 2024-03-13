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

    # CRUD operations for Chart
    def add_chart(self, chart):
        query = "INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (chart.chartID, chart.weight, chart.height, chart.bloodPressure, chart.temperature, chart.prescriptions, chart.diagnoses, chart.allergies, chart.date)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_chart_by_id(self, chartID):
        query = "SELECT * FROM Chart WHERE chartID = %s"
        self.cursor.execute(query, (chartID,))
        result = self.cursor.fetchone()
        if result:
            chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date = result
            return Chart(chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date)
        else:
            return None

    def update_chart(self, chart):
        query = "UPDATE Chart SET weight=%s, height=%s, bloodPressure=%s, temperature=%s, prescriptions=%s, diagnoses=%s, allergies=%s, date=%s WHERE chartID=%s"
        values = (chart.weight, chart.height, chart.bloodPressure, chart.temperature, chart.prescriptions, chart.diagnoses, chart.allergies, chart.date, chart.chartID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_chart(self, chartID):
        query = "DELETE FROM Chart WHERE chartID = %s"
        self.cursor.execute(query, (chartID,))
        self.connection.commit()

    # CRUD operations for Prescription, InsurancePolicy, Bill, and Payment can be similarly implemented

    def close(self):
        self.cursor.close()
        self.connection.close()

# Example usage
if __name__ == "__main__":
    # Replace these values with your MySQL server credentials
    db = PatientAccountDatabase(host="localhost", user="your_username", password="your_password", database="MedPortal")

    # Example operations
    # Add a new patient account
    new_patient = PatientAccount(accountID="123456", age=30, ssn="123-45-6789", chart="789012", insurancePolicy="456789", bills="789012")
    db.add_patient_account(new_patient)

    # Retrieve a patient account by ID
    retrieved_patient = db.get_patient_account_by_id("123456")
    if retrieved_patient:
        print("Retrieved patient:", retrieved_patient.accountID, retrieved_patient.age)
    else:
        print("Patient not found")

    # Close the database connection
    db.close()
