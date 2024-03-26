class Account:
    def __init__(self, accountID, email, phoneNumber, address):
        self.accountID = accountID
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address

    def __str__(self) -> str:
        return self.accountID

    def inserts(self) -> list[str]:
        query = "INSERT INTO Account (accountID, email, phoneNumber, address) VALUES (%s, %s, %s, %s)"
        values = (self.accountID, self.email, self.phoneNumber, self.address)

        return [query.format(values)]

    def updates(self) -> list[str]:
        query = "UPDATE Account SET email=%s, phoneNumber=%s, address=%s WHERE accountID=%s"
        values = (self.email, self.phoneNumber, self.address, self.accountID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT accountID, email, phoneNumber, address FROM Account WHERE accountID = %s"


class InsurancePolicy:
    def __init__(self, insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount):
        self.insurancePolicyID = insurancePolicyID
        self.insuranceName = insuranceName
        self.insurancePolicyNumber = insurancePolicyNumber
        self.copayAmount = copayAmount

    def __str__(self) -> str:
        return self.insurancePolicyID

    def inserts(self) -> list[str]:
        query = "INSERT INTO InsurancePolicy (insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount) VALUES (%s, %s, %s, %s)"
        values = (self.insurancePolicyID, self.insuranceName, self.insurancePolicyNumber, self.copayAmount)

        return [query.format(values)]

    def updates(self) -> list[str]:
        query = "UPDATE InsurancePolicy SET insuranceName=%s, insurancePolicyNumber=%s, copayAmount=%s WHERE insurancePolicyID=%s"
        values = (self.insuranceName, self.insurancePolicyNumber, self.copayAmount, self.insurancePolicyID)
        
        return [query.format(values)]

    def select() -> str:
        return "SELECT insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount FROM InsurancePolicy WHERE insurancePolicyID = %s"


class PatientAccount(Account):
    def __init__(self, patientAccountID, email, phoneNumber, address, age, ssn, insurancePolicy: InsurancePolicy):
        Account.__init__(self, patientAccountID, email, phoneNumber, address)
        self.patientAccountID = patientAccountID
        self.age = age
        self.ssn = ssn
        self.insurancePolicy = insurancePolicy

    def __str__(self) -> str:
        return self.accountID

    def inserts(self) -> list[str]:
        query = "INSERT INTO PatientAccount (patientAccountID, age, ssn, insurancePolicyID) VALUES (%s, %s, %s, %s)"
        values = (self.patientAccountID, self.age, self.ssn, self.insurancePolicy)
        
        return Account.inserts(self) + [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE PatientAccount SET age=%s, ssn=%s, insurancePolicyID=%s WHERE patientAccountID=%s"
        values = (self.age, self.ssn, self.insurancePolicy, self.patientAccountID)

        return Account.inserts(self) + [query.format(values)]
    
    def select() -> str:
        return "SELECT patientAccountID, email, phoneNumber, address, age, ssn, insurancePolicyID FROM PatientAccount INNER JOIN Account ON PatientAccount.patientAccountID = Account.accountID WHERE accountID=%s"
        

class StaffAccount(Account):
    def __init__(self, staffAccountID, email, phoneNumber, address, role, accountID):
        Account.__init__(self, accountID, email, phoneNumber, address)
        self.staffAccountID = staffAccountID
        self.role = role

    def __str__(self) -> str:
        return self.accountID

    def inserts(self) -> list[str]:
        query = "INSERT INTO StaffAccount (staffAccountID, role, accountID) VALUES (%s, %s, %s)"
        values = (self.staffAccountID, self.role, self.accountID)

        return Account.inserts(self) + [query.format(values)]

    def updates(self) -> list[str]:
        query = "UPDATE StaffAccount SET role=%s, accountID=%s WHERE staffAccountID=%s"
        values = (self.role, self.accountID, self.staffAccountID)

        return Account.inserts(self) + [query.format(values)]
    
    def select() -> str:
        return "SELECT staffAccountID, email, phoneNumber, address, calendarID, inboxID, outboxID, role, accountID FROM StaffAccount INNER JOIN Account ON StaffAccount.accountID = Account.accountID WHERE staffAccountID=%s"


class Chart:
    def __init__(self, chartID, weight, height, bloodPressure, temperature, diagnoses, allergies, date, patientAccountID):
        self.chartID = chartID
        self.weight = weight
        self.height = height
        self.bloodPressure = bloodPressure
        self.temperature = temperature
        self.diagnoses = diagnoses
        self.allergies = allergies
        self.date = date
        self.patientAccountID = patientAccountID

    def __str__(self) -> str:
        return self.chartID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, diagnoses, allergies, date, patientAccountID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.chartID, self.weight, self.height, self.bloodPressure, self.temperature, self.diagnoses, self.allergies, self.date, self.patientAccountID)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Chart SET weight=%s, height=%s, bloodPressure=%s, temperature=%s, diagnoses=%s, allergies=%s, date=%s, patientAccountID=%s WHERE chartID=%s"
        values = (self.weight, self.height, self.bloodPressure, self.temperature, self.diagnoses, self.allergies, self.date, self.patientAccountID, self.chartID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT chartID, weight, height, bloodPressure, temperature, diagnoses, allergies, date, patientAccountID FROM Chart WHERE chartID = %s"


class Prescription:
    def __init__(self, prescriptionID, drug, dosage, frequency, date, pharmacyID, patientAccountID):
        self.prescriptionID = prescriptionID
        self.drug = drug
        self.dosage = dosage
        self.frequency = frequency
        self.date = date
        self.pharmacyID = pharmacyID
        self.patientAccountID = patientAccountID

    def __str__(self) -> str:
        return self.prescriptionID

    def inserts(self) -> list[str]:
        query = "INSERT INTO Prescription (prescriptionID, drug, dosage, frequency, date, pharmacyID, patientAccountID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (self.prescriptionID, self.drug, self.dosage, self.frequency, self.date, self.pharmacyID, self.patientAccountID)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Prescription SET drug=%s, dosage=%s, frequency=%s, date=%s, pharmacyID=%s, patientAccountID=%s WHERE prescriptionID=%s"
        values = (self.drug, self.dosage, self.frequency, self.date, self.pharmacyID, self.patientAccountID, self.prescriptionID)
    
        return [query.format(values)]
    
    def select() -> str:
        return "SELECT prescriptionID, drug, dosage, frequency, date, pharmacyID, patientAccountID FROM Prescription WHERE prescriptionID = %s"


class Pharmacy:
    def __init__(self, pharmacyID, name, address, phoneNumber):
        self.pharmacyID = pharmacyID
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    def __str__(self) -> str:
        return self.pharmacyID

    def inserts(self) -> list[str]:
        query = "INSERT INTO Pharmacy (pharmacyID, name, address, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (self.pharmacyID, self.name, self.address, self.phoneNumber)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Pharmacy SET name=%s, address=%s, phoneNumber=%s WHERE pharmacyID=%s"
        values = (self.name, self.address, self.phoneNumber, self.pharmacyID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT pharmacyID, name, address, phoneNumber FROM Pharmacy WHERE pharmacyID = %s"


class Test:
    def __init__(self, testID, description, date, labID, patientAccountID):
        self.testID = testID
        self.description = description
        self.date = date
        self.labID = labID
        self.patientAccountID = patientAccountID

    def __str__(self) -> str:
        return self.testID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO Test (testID, description, date, labID, patientAccountID) VALUES (%s, %s, %s, %s, %s)"
        values = (self.testID, self.description, self.date, self.labID, self.patientAccountID)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Test SET description=%s, date=%s, labID=%s, patientAccountID=%s WHERE testID = %s"
        values = (self.description, self.date, self.labID, self.patientAccountID, self.testID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT testID, description, date, labID, patientAccountID FROM Test WHERE testID = %s"


class TestResult:
    def __init__(self, testResultID, testID, date, result):
        self.testResultID = testResultID
        self.testID = testID
        self.date = date
        self.result = result

    def __str__(self) -> str:
        return self.testResultID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO TestResult (testResultID, testID, date, result) VALUES (%s, %s, %s, %s)"
        values = (self.testResultID, self.testID, self.date, self.result)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE TestResult SET testID=%s, date=%s, result=%s WHERE testResultID=%s"
        values = (self.testID, self.date, self.result, self.testResultID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT testResultID, testID, date, result FROM TestResult WHERE testResultID = %s"


class Laboratory:
    def __init__(self, labID, name, address, phoneNumber):
        self.labID = labID
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    def __str__(self) -> str:
        return self.labID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO Laboratory (labID, name, address, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (self.labID, self.name, self.address, self.phoneNumber)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Laboratory SET name=%s, address=%s, phoneNumber=%s WHERE labID=%s"
        values = (self.name, self.address, self.phoneNumber, self.labID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT labID, name, address, phoneNumber FROM Laboratory WHERE labID = %s"


class Appointment:
    def __init__(self, appointmentID, description, date, time, patientAccountID, doctorAccountID):
        self.appointmentID = appointmentID
        self.description = description
        self.date = date
        self.time = time
        self.patientAccountID = patientAccountID
        self.doctorAccountID = doctorAccountID

    def __str__(self) -> str:
        return self.appointmentID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO Appointment (appointmentID, description, date, time, patientAccountID, doctorAccountID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.appointmentID, self.description, self.date, self.time, self.patientAccountID, self.doctorAccountID)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Appointment SET description=%s, date=%s, time=%s, patientAccountID=%s, doctorAccountID=%s WHERE appointmentID=%s"
        values = (self.description, self.date, self.time, self.patientAccountID, self.doctorAccountID, self.appointmentID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT appointmentID, description, date, time, patientAccountID, doctorAccountID FROM Appointment WHERE appointmentID = %s"


class Bill:
    def __init__(self, billID, description, amount, dateIssued, dueDate, patientAccountID):
        self.billID = billID
        self.description = description
        self.amount = amount
        self.dateIssued = dateIssued
        self.dueDate = dueDate
        self.patientAccountID = patientAccountID

    def __str__(self) -> str:
        return self.billID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO Bill (billID, description, amount, dateIssued, dueDate, patientAccountID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.billID, self.description, self.amount, self.dateIssued, self.dueDate, self.patientAccountID)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Bill SET description=%s, amount=%s, dateIssued=%s, dueDate=%s, patientAccountID=%s WHERE billID=%s"
        values = (self.description, self.amount, self.dateIssued, self.dueDate, self.patientAccountID, self.billID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT billID, description, amount, dateIssued, dueDate, patientAccountID FROM Bill WHERE billID = %s"


class Payment:
    def __init__(self, paymentID, billID, amount, date):
        self.paymentID = paymentID
        self.billID = billID
        self.amount = amount
        self.date = date

    def __str__(self) -> str:
        return self.paymentID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO Payment (paymentID, billID, amount, date) VALUES (%s, %s, %s, %s)"
        values = (self.paymentID, self.billID, self.amount, self.date)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Payment SET billID=%s, amount=%s, date=%s WHERE paymentID=%s"
        values = (self.billID, self.amount, self.date, self.paymentID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT paymentID, billID, amount, date FROM Payment WHERE paymentID = %s"


class Reminder:
    def __init__(self, reminderID, description, date, time, accountID):
        self.reminderID = reminderID
        self.description = description
        self.date = date
        self.time = time
        self.accountID = accountID

    def __str__(self) -> str:
        return self.reminderID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO Reminder (reminderID, description, date, time, accountID) VALUES (%s, %s, %s, %s, %s)"
        values = (self.reminderID, self.description, self.date, self.time, self.accountID)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Reminder SET description=%s, date=%s, time=%s, accountID=%s WHERE reminderID=%s"
        values = (self.description, self.date, self.time, self.accountID, self.reminderID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT reminderID, description, date, time, accountID FROM Reminder WHERE reminderID = %s"


class Message:
    def __init__(self, messageID, date, time, messageText, senderAccountID, recipientAccountID):
        self.messageID = messageID
        self.date = date
        self.time = time
        self.messageText = messageText
        self.senderAccountID = senderAccountID
        self.recipientAccountID = recipientAccountID

    def __str__(self) -> str:
        return self.messageID
    
    def inserts(self) -> list[str]:
        query = "INSERT INTO Message (messageID, date, time, messageText, senderAccountID, recipientAccountID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.messageID, self.date, self.time, self.messageText, self.senderAccountID, self.recipientAccountID)

        return [query.format(values)]
    
    def updates(self) -> list[str]:
        query = "UPDATE Message SET date=%s, time=%s, messageText=%s, senderAccountID=%s, recipientAccountID=%s WHERE messageID=%s"
        values = (self.date, self.time, self.messageText, self.senderAccountID, self.recipientAccountID, self.messageID)

        return [query.format(values)]
    
    def select() -> str:
        return "SELECT messageID, date, time, messageText, senderAccountID, recipientAccountID FROM Message WHERE messageID = %s"
    