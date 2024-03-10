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

    # CRUD operations for Account
    def add_account(self, account):
        query = "INSERT INTO Account (accountID, email, phoneNumber, address, calendarID, inboxID, outboxID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (account.accountID, account.email, account.phoneNumber, account.address, account.calendarID, account.inboxID, account.outboxID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_account_by_id(self, accountID):
        query = "SELECT * FROM Account WHERE accountID = %s"
        self.cursor.execute(query, (accountID,))
        result = self.cursor.fetchone()
        if result:
            accountID, email, phoneNumber, address, calendarID, inboxID, outboxID = result
            return Account(accountID, email, phoneNumber, address, calendarID, inboxID, outboxID)
        else:
            return None

    def update_account(self, account):
        query = "UPDATE Account SET email=%s, phoneNumber=%s, address=%s, calendarID=%s, inboxID=%s, outboxID=%s WHERE accountID=%s"
        values = (account.email, account.phoneNumber, account.address, account.calendarID, account.inboxID, account.outboxID, account.accountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_account(self, accountID):
        query = "DELETE FROM Account WHERE accountID = %s"
        self.cursor.execute(query, (accountID,))
        self.connection.commit()
