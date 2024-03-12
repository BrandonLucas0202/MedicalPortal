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


# CRUD operations for TestResult
    def add_test_result(self, test_result):
        query = "INSERT INTO TestResult (testResultID, testID, date, result) VALUES (%s, %s, %s, %s)"
        values = (test_result.testResultID, test_result.testID, test_result.date, test_result.result)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_test_result_by_id(self, testResultID):
        query = "SELECT * FROM TestResult WHERE testResultID = %s"
        self.cursor.execute(query, (testResultID,))
        result = self.cursor.fetchone()
        if result:
            testResultID, testID, date, result = result
            return TestResult(testResultID, testID, date, result)
        else:
            return None

    def update_test_result(self, test_result):
        query = "UPDATE TestResult SET testID=%s, date=%s, result=%s WHERE testResultID=%s"
        values = (test_result.testID, test_result.date, test_result.result, test_result.testResultID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_test_result(self, testResultID):
        query = "DELETE FROM TestResult WHERE testResultID = %s"
        self.cursor.execute(query, (testResultID,))
        self.connection.commit()
