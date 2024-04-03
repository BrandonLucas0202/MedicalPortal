"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Database Test object and TestResult object.
"""
from model.model import Model, PermanentModel, QueryModel

class Test(PermanentModel):
    def __init__(self, testID) -> None:
        Model.__init__(self, "Test", [
           "testID", "description", "date", "time", "labID", "patientAccountID"
        ], {"testID": testID})
        self.__testID = testID

    def getTestID(self):
        return self.__testID
    
class TestWithResult(QueryModel):
    def __init__(self, testID) -> None:
        Model.__init__(self, "Test LEFT JOIN TestResult ON Test.testID = TestResult.testID", [
           "Test.testID AS testID", "description", "date", "time", "labID", "patientAccountID", "testResultID", "resultDate", "result"
        ], {"testID": testID})
        self.__testID = testID

    def getTestID(self):
        return self.__testID
    
class TestResult(PermanentModel):
    def __init__(self, testResultID) -> None:
        Model.__init__(self, "TestResult", [
           "testResultID", "testID", "date", "result"
        ], {"testResultID": testResultID})
        self.__testResultID = testResultID

    def getTestResultID(self):
        return self.__testResultID