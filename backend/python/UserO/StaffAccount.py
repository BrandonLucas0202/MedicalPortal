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

  # CRUD operations for StaffAccount
    def add_staff_account(self, staff_account):
        query = "INSERT INTO StaffAccount (staffAccountID, role, accountID) VALUES (%s, %s, %s)"
        values = (staff_account.staffAccountID, staff_account.role, staff_account.accountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_staff_account_by_id(self, staffAccountID):
        query = "SELECT * FROM StaffAccount WHERE staffAccountID = %s"
        self.cursor.execute(query, (staffAccountID,))
        result = self.cursor.fetchone()
        if result:
            staffAccountID, role, accountID = result
            return StaffAccount(staffAccountID, role, accountID)
        else:
            return None

    def update_staff_account(self, staff_account):
        query = "UPDATE StaffAccount SET role=%s, accountID=%s WHERE staffAccountID=%s"
        values = (staff_account.role, staff_account.accountID, staff_account.staffAccountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_staff_account(self, staffAccountID):
        query = "DELETE FROM StaffAccount WHERE staffAccountID = %s"
        self.cursor.execute(query, (staffAccountID,))
        self.connection.commit()

def close(self):
        self.cursor.close()
        self.connection.close()
