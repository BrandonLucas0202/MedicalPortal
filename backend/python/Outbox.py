# CRUD operations for Outbox
    def add_outbox(self, outbox):
        query = "INSERT INTO Outbox (outboxID, messages) VALUES (%s, %s)"
        values = (outbox.outboxID, outbox.messages)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_outbox_by_id(self, outboxID):
        query = "SELECT * FROM Outbox WHERE outboxID = %s"
        self.cursor.execute(query, (outboxID,))
        result = self.cursor.fetchone()
        if result:
            outboxID, messages = result
            return Outbox(outboxID, messages)
        else:
            return None

    def update_outbox(self, outbox):
        query = "UPDATE Outbox SET messages=%s WHERE outboxID=%s"
        values = (outbox.messages, outbox.outboxID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_outbox(self, outboxID):
        query = "DELETE FROM Outbox WHERE outboxID = %s"
        self.cursor.execute(query, (outboxID,))
        self.connection.commit()
