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

    # CRUD operations for Bill
    def add_bill(self, bill):
        query = "INSERT INTO Bill (billID, amount, dateIssued, dueDate, patientAccountID) VALUES (%s, %s, %s, %s, %s)"
        values = (bill.billID, bill.amount, bill.dateIssued, bill.dueDate, bill.patientAccountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_bill_by_id(self, billID):
        query = "SELECT * FROM Bill WHERE billID = %s"
        self.cursor.execute(query, (billID,))
        result = self.cursor.fetchone()
        if result:
            billID, amount, dateIssued, dueDate, patientAccountID = result
            return Bill(billID, amount, dateIssued, dueDate, patientAccountID)
        else:
            return None

    def update_bill(self, bill):
        query = "UPDATE Bill SET amount=%s, dateIssued=%s, dueDate=%s, patientAccountID=%s WHERE billID=%s"
        values = (bill.amount, bill.dateIssued, bill.dueDate, bill.patientAccountID, bill.billID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_bill(self, billID):
        query = "DELETE FROM Bill WHERE billID = %s"
        self.cursor.execute(query, (billID,))
        self.connection.commit()

    # Other methods...

# Example usage
if __name__ == "__main__":
    # Replace these values with your MySQL server credentials
    db = PatientAccountDatabase(host="localhost", user="your_username", password="your_password", database="MedPortal")

    # Example operations
    # Add a new bill
    new_bill = Bill(billID="123", amount=100, dateIssued="2024-03-09", dueDate="2024-03-19", patientAccountID="789")
    db.add_bill(new_bill)

    # Retrieve a bill by ID
    retrieved_bill = db.get_bill_by_id("123")
    if retrieved_bill:
        print("Retrieved bill:", retrieved_bill.billID, retrieved_bill.amount)
    else:
        print("Bill not found")

    # Close the database connection
    db.close()
