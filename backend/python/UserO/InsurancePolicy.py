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

    # CRUD operations for InsurancePolicy
    def add_insurance_policy(self, insurance_policy):
        query = "INSERT INTO InsurancePolicy (insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount) VALUES (%s, %s, %s, %s)"
        values = (insurance_policy.insurancePolicyID, insurance_policy.insuranceName, insurance_policy.insurancePolicyNumber, insurance_policy.copayAmount)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_insurance_policy_by_id(self, insurancePolicyID):
        query = "SELECT * FROM InsurancePolicy WHERE insurancePolicyID = %s"
        self.cursor.execute(query, (insurancePolicyID,))
        result = self.cursor.fetchone()
        if result:
            insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount = result
            return InsurancePolicy(insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount)
        else:
            return None

    def update_insurance_policy(self, insurance_policy):
        query = "UPDATE InsurancePolicy SET insuranceName=%s, insurancePolicyNumber=%s, copayAmount=%s WHERE insurancePolicyID=%s"
        values = (insurance_policy.insuranceName, insurance_policy.insurancePolicyNumber, insurance_policy.copayAmount, insurance_policy.insurancePolicyID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_insurance_policy(self, insurancePolicyID):
        query = "DELETE FROM InsurancePolicy WHERE insurancePolicyID = %s"
        self.cursor.execute(query, (insurancePolicyID,))
        self.connection.commit()

    # Other methods...

# Example usage
if __name__ == "__main__":
    # Replace these values with your MySQL server credentials
    db = PatientAccountDatabase(host="localhost", user="your_username", password="your_password", database="MedPortal")

    # Example operations
    # Add a new insurance policy
    new_insurance_policy = InsurancePolicy(insurancePolicyID="789", insuranceName="InsuranceCo", insurancePolicyNumber="123456", copayAmount=20)
    db.add_insurance_policy(new_insurance_policy)

    # Retrieve an insurance policy by ID
    retrieved_insurance_policy = db.get_insurance_policy_by_id("789")
    if retrieved_insurance_policy:
        print("Retrieved insurance policy:", retrieved_insurance_policy.insurancePolicyID, retrieved_insurance_policy.insuranceName)
    else:
        print("Insurance policy not found")

    # Close the database connection
    db.close()
