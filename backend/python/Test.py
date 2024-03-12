# CRUD operations for Test
    def add_test(self, test):
        query = "INSERT INTO Test (testID, type, date, labID) VALUES (%s, %s, %s, %s)"
        values = (test.testID, test.type, test.date, test.labID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_test_by_id(self, testID):
        query = "SELECT * FROM Test WHERE testID = %s"
        self.cursor.execute(query, (testID,))
        result = self.cursor.fetchone()
        if result:
            testID, type, date, labID = result
            return Test(testID, type, date, labID)
        else:
            return None

    def update_test(self, test):
        query = "UPDATE Test SET type = %s, date = %s, labID = %s WHERE testID = %s"
        values = (test.type, test.date, test.labID, test.testID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_test(self, testID):
        query = "DELETE FROM Test WHERE testID = %s"
        self.cursor.execute(query, (testID,))
        self.connection.commit()
