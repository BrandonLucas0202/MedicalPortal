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

 # CRUD operations for Message
    def add_message(self, message):
        query = "INSERT INTO Message (messageID, senderAccountID, recipientAccountID, messageText) VALUES (%s, %s, %s, %s)"
        values = (message.messageID, message.senderAccountID, message.recipientAccountID, message.messageText)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_message_by_id(self, messageID):
        query = "SELECT * FROM Message WHERE messageID = %s"
        self.cursor.execute(query, (messageID,))
        result = self.cursor.fetchone()
        if result:
            messageID, senderAccountID, recipientAccountID, messageText = result
            return Message(messageID, senderAccountID, recipientAccountID, messageText)
        else:
            return None

    def update_message(self, message):
        query = "UPDATE Message SET senderAccountID=%s, recipientAccountID=%s, messageText=%s WHERE messageID=%s"
        values = (message.senderAccountID, message.recipientAccountID, message.messageText, message.messageID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_message(self, messageID):
        query = "DELETE FROM Message WHERE messageID = %s"
        self.cursor.execute(query, (messageID,))
        self.connection.commit()
