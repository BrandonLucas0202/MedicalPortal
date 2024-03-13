# CRUD operations for Inbox
    def add_inbox(self, inbox):
        query = "INSERT INTO Inbox (inboxID, messages) VALUES (%s, %s)"
        values = (inbox.inboxID, inbox.messages)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_inbox_by_id(self, inboxID):
        query = "SELECT * FROM Inbox WHERE inboxID = %s"
        self.cursor.execute(query, (inboxID,))
        result = self.cursor.fetchone()
        if result:
            inboxID, messages = result
            return Inbox(inboxID, messages)
        else:
            return None

    def update_inbox(self, inbox):
        query = "UPDATE Inbox SET messages=%s WHERE inboxID=%s"
        values = (inbox.messages, inbox.inboxID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_inbox(self, inboxID):
        query = "DELETE FROM Inbox WHERE inboxID = %s"
        self.cursor.execute(query, (inboxID,))
        self.connection.commit()
