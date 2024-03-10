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

    # CRUD operations for Payment
    def add_payment(self, payment):
        query = "INSERT INTO Payment (paymentID, billID, amount, date) VALUES (%s, %s, %s, %s)"
        values = (payment.paymentID, payment.billID, payment.amount, payment.date)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_payment_by_id(self, paymentID):
        query = "SELECT * FROM Payment WHERE paymentID = %s"
        self.cursor.execute(query, (paymentID,))
        result = self.cursor.fetchone()
        if result:
            paymentID, billID, amount, date = result
            return Payment(paymentID, billID, amount, date)
        else:
            return None

    def update_payment(self, payment):
        query = "UPDATE Payment SET billID=%s, amount=%s, date=%s WHERE paymentID=%s"
        values = (payment.billID, payment.amount, payment.date, payment.paymentID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_payment(self, paymentID):
        query = "DELETE FROM Payment WHERE paymentID = %s"
        self.cursor.execute(query, (paymentID,))
        self.connection.commit()

    # Other methods...

# Example usage
if __name__ == "__main__":
    # Replace these values with your MySQL server credentials
    db = PatientAccountDatabase(host="localhost", user="your_username", password="your_password", database="MedPortal")

    # Example operations
    # Add a new payment
    new_payment = Payment(paymentID="456", billID="123", amount=50, date="2024-03-09")
    db.add_payment(new_payment)

    # Retrieve a payment by ID
    retrieved_payment = db.get_payment_by_id("456")
    if retrieved_payment:
        print("Retrieved payment:", retrieved_payment.paymentID, retrieved_payment.amount)
    else:
        print("Payment not found")

    # Close the database connection
    db.close()
