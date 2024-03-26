class Account:
    def __init__(self, accountID, email, phoneNumber, address, calendarID, inboxID, outboxID):
        self.accountID = accountID
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.calendarID = calendarID
        self.inboxID = inboxID
        self.outboxID = outboxID

    # CRUD operations for Account
    def inserts(self) -> list[str]:
        query = "INSERT INTO Account (accountID, email, phoneNumber, address, calendarID, inboxID, outboxID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (self.accountID, self.email, self.phoneNumber, self.address, self.calendarID, self.inboxID, self.outboxID)

        return [query.format(values)]

    def updates(self) -> list[str]:
        query = "UPDATE Account SET email=%s, phoneNumber=%s, address=%s, calendarID=%s, inboxID=%s, outboxID=%s WHERE accountID=%s"
        values = (self.email, self.phoneNumber, self.address, self.calendarID, self.inboxID, self.outboxID, self.accountID)

        return [query.format(values)]

class PatientAccount(Account):
    def __init__(self, accountID, email, phoneNumber, address, calendarID, inboxID, outboxID, age, ssn, chart, insurancePolicy, bills):
        Account.__init__(self, accountID, email, phoneNumber, address, calendarID, inboxID, outboxID)
        self.age = age
        self.ssn = ssn
        self.chart = chart
        self.insurancePolicy = insurancePolicy
        self.bills = bills

    def inserts(self) -> list[str]:
        query = "INSERT INTO PatientAccount (accountID, age, ssn, chart, insurancePolicy, bills) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.accountID, self.age, self.ssn, self.chart, self.insurancePolicy, self.bills)
        
        return [query.format(values)] + Account.inserts(self)
    
    def updates(self) -> list[str]:
        query = "UPDATE PatientAccount SET age=%s, ssn=%s, chart=%s, insurancePolicy=%s, bills=%s WHERE accountID=%s"
        values = (self.age, self.ssn, self.chart, self.insurancePolicy, self.bills, self.accountID)

        return [query.format(values)] + Account.updates(self)
    
    def select() -> str:
        return "SELECT accountID, email, phoneNumber, address, calendarID, inboxID, outboxID, age, ssn, chart, insurancePolicy, bills FROM PatientAccount INNER JOIN Account ON PatientAccount.accountID = Account.accountID WHERE accountID=%s"
        

class StaffAccount(Account):
    def __init__(self, staffAccountID, email, phoneNumber, address, calendarID, inboxID, outboxID, role, accountID):
        Account.__init__(self, accountID, email, phoneNumber, address, calendarID, inboxID, outboxID)
        self.staffAccountID = staffAccountID
        self.role = role

    # CRUD operations for StaffAccount
    def inserts(self) -> list[str]:
        query = "INSERT INTO StaffAccount (staffAccountID, role, accountID) VALUES (%s, %s, %s)"
        values = (self.staffAccountID, self.role, self.accountID)

        return [query.format(values)] + Account.inserts(self)

    def updates(self) -> list[str]:
        query = "UPDATE StaffAccount SET role=%s, accountID=%s WHERE staffAccountID=%s"
        values = (self.role, self.accountID, self.staffAccountID)

        return [query.format(values)] + Account.updates(self)
    
    def select() -> str:
        return "SELECT staffAccountID, email, phoneNumber, address, calendarID, inboxID, outboxID, role, accountID FROM StaffAccount INNER JOIN Account ON StaffAccount.accountID = Account.accountID WHERE staffAccountID=%s"

class Chart:
    def __init__(self, chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date):
        self.chartID = chartID
        self.weight = weight
        self.height = height
        self.bloodPressure = bloodPressure
        self.temperature = temperature
        self.prescriptions = prescriptions
        self.diagnoses = diagnoses
        self.allergies = allergies
        self.date = date

    # CRUD operations for Chart
    def inserts(self) -> list[str]:
        query = "INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (chart.chartID, chart.weight, chart.height, chart.bloodPressure, chart.temperature, chart.prescriptions, chart.diagnoses, chart.allergies, chart.date)

    def updates(self) -> list[str]:
        query = "UPDATE Chart SET weight=%s, height=%s, bloodPressure=%s, temperature=%s, prescriptions=%s, diagnoses=%s, allergies=%s, date=%s WHERE chartID=%s"
        values = (chart.weight, chart.height, chart.bloodPressure, chart.temperature, chart.prescriptions, chart.diagnoses, chart.allergies, chart.date, chart.chartID)


class Prescription:
    def __init__(self, prescriptionID, drug, dosage, frequency, date, pharmacyID):
        self.prescriptionID = prescriptionID
        self.drug = drug
        self.dosage = dosage
        self.frequency = frequency
        self.date = date
        self.pharmacyID = pharmacyID

    # CRUD operations for Prescription
    def inserts(self) -> list[str]:
        query = "INSERT INTO Prescription (prescriptionID, drug, dosage, frequency, date, pharmacyID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (prescription.prescriptionID, prescription.drug, prescription.dosage, prescription.frequency, prescription.date, prescription.pharmacyID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def updates(self) -> list[str]:
        query = "UPDATE Prescription SET drug=%s, dosage=%s, frequency=%s, date=%s, pharmacyID=%s WHERE prescriptionID=%s"
        values = (prescription.drug, prescription.dosage, prescription.frequency, prescription.date, prescription.pharmacyID, prescription.prescriptionID)


class InsurancePolicy:
    def __init__(self, insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount):
        self.insurancePolicyID = insurancePolicyID
        self.insuranceName = insuranceName
        self.insurancePolicyNumber = insurancePolicyNumber
        self.copayAmount = copayAmount

    # CRUD operations for InsurancePolicy
    def inserts(self) -> list[str]:
        query = "INSERT INTO InsurancePolicy (insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount) VALUES (%s, %s, %s, %s)"
        values = (insurance_policy.insurancePolicyID, insurance_policy.insuranceName, insurance_policy.insurancePolicyNumber, insurance_policy.copayAmount)

    def updates(self) -> list[str]:
        query = "UPDATE InsurancePolicy SET insuranceName=%s, insurancePolicyNumber=%s, copayAmount=%s WHERE insurancePolicyID=%s"
        values = (insurance_policy.insuranceName, insurance_policy.insurancePolicyNumber, insurance_policy.copayAmount, insurance_policy.insurancePolicyID)


class Pharmacy:
    def __init__(self, pharmacyID, name, address, phoneNumber):
        self.pharmacyID = pharmacyID
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    # CRUD operations for Pharmacy
    def inserts(self) -> list[str]:
        query = "INSERT INTO Pharmacy (pharmacyID, name, address, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (pharmacy.pharmacyID, pharmacy.name, pharmacy.address, pharmacy.phoneNumber)

    def updates(self) -> list[str]:
        query = "UPDATE Pharmacy SET name=%s, address=%s, phoneNumber=%s WHERE pharmacyID=%s"
        values = (pharmacy.name, pharmacy.address, pharmacy.phoneNumber, pharmacy.pharmacyID)


class Inbox:
    def __init__(self, inboxID, messages):
        self.inboxID = inboxID
        self.messages = messages

    # CRUD operations for Inbox
    def inserts(self) -> list[str]:
        query = "INSERT INTO Inbox (inboxID, messages) VALUES (%s, %s)"
        values = (inbox.inboxID, inbox.messages)

    def updates(self) -> list[str]:
        query = "UPDATE Inbox SET messages=%s WHERE inboxID=%s"
        values = (inbox.messages, inbox.inboxID)


class Outbox:
    def __init__(self, outboxID, messages):
        self.outboxID = outboxID
        self.messages = messages

    # CRUD operations for Outbox
    def inserts(self) -> list[str]:
        query = "INSERT INTO Outbox (outboxID, messages) VALUES (%s, %s)"
        values = (outbox.outboxID, outbox.messages)

    def updates(self) -> list[str]:
        query = "UPDATE Outbox SET messages=%s WHERE outboxID=%s"
        values = (outbox.messages, outbox.outboxID)


class Test:
    def __init__(self, testID, type, date, labID):
        self.testID = testID
        self.type = type
        self.date = date
        self.labID = labID

    # CRUD operations for Test
    def inserts(self) -> list[str]:
        query = "INSERT INTO Test (testID, type, date, labID) VALUES (%s, %s, %s, %s)"
        values = (test.testID, test.type, test.date, test.labID)

    def updates(self) -> list[str]:
        query = "UPDATE Test SET type = %s, date = %s, labID = %s WHERE testID = %s"
        values = (test.type, test.date, test.labID, test.testID)

class TestResult:
    def __init__(self, testResultID, testID, date, result):
        self.testResultID = testResultID
        self.testID = testID
        self.date = date
        self.result = result

    # CRUD operations for TestResult
    def inserts(self) -> list[str]:
        query = "INSERT INTO TestResult (testResultID, testID, date, result) VALUES (%s, %s, %s, %s)"
        values = (test_result.testResultID, test_result.testID, test_result.date, test_result.result)

    def updates(self) -> list[str]:
        query = "UPDATE TestResult SET testID=%s, date=%s, result=%s WHERE testResultID=%s"
        values = (test_result.testID, test_result.date, test_result.result, test_result.testResultID)


class Laboratory:
    def __init__(self, labID, name, address, phoneNumber):
        self.labID = labID
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    # CRUD operations for Laboratory
    def inserts(self) -> list[str]:
        query = "INSERT INTO Laboratory (labID, name, address, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (laboratory.labID, laboratory.name, laboratory.address, laboratory.phoneNumber)

    def updates(self) -> list[str]:
        query = "UPDATE Laboratory SET name=%s, address=%s, phoneNumber=%s WHERE labID=%s"
        values = (laboratory.name, laboratory.address, laboratory.phoneNumber, laboratory.labID)


class Calendar:
    def __init__(self, calendarID):
        self.calendarID = calendarID

     # CRUD operations for Calendar
    def inserts(self) -> list[str]:
        query = "INSERT INTO Calendar (calendarID) VALUES (%s)"
        values = (calendar.calendarID,)

    def updates(self) -> list[str]:
        query = "UPDATE Calendar SET calendarID = %s WHERE calendarID = %s"
        values = (calendar.calendarID, calendar.calendarID)


class Appointment:
    def __init__(self, appointmentID, type, date, time, patientAccountID, doctorAccountID):
        self.appointmentID = appointmentID
        self.type = type
        self.date = date
        self.time = time
        self.patientAccountID = patientAccountID
        self.doctorAccountID = doctorAccountID

    # CRUD operations for Appointment
    def inserts(self) -> list[str]:
        query = "INSERT INTO Appointment (appointmentID, doctorID, patientID, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (appointment.appointmentID, appointment.doctorID, appointment.patientID, appointment.date, appointment.time, appointment.status)

    def updates(self) -> list[str]:
        query = "UPDATE Appointment SET doctorID=%s, patientID=%s, date=%s, time=%s, status=%s WHERE appointmentID=%s"
        values = (appointment.doctorID, appointment.patientID, appointment.date, appointment.time, appointment.status, appointment.appointmentID)


class Bill:
    def __init__(self, billID, amount, dateIssued, dueDate, patientAccountID):
        self.billID = billID
        self.amount = amount
        self.dateIssued = dateIssued
        self.dueDate = dueDate
        self.patientAccountID = patientAccountID

    # CRUD operations for Bill
    def inserts(self) -> list[str]:
        query = "INSERT INTO Bill (billID, amount, dateIssued, dueDate, patientAccountID) VALUES (%s, %s, %s, %s, %s)"
        values = (bill.billID, bill.amount, bill.dateIssued, bill.dueDate, bill.patientAccountID)

    def updates(self) -> list[str]:
        query = "UPDATE Bill SET amount=%s, dateIssued=%s, dueDate=%s, patientAccountID=%s WHERE billID=%s"
        values = (bill.amount, bill.dateIssued, bill.dueDate, bill.patientAccountID, bill.billID)


class Payment:
    def __init__(self, paymentID, billID, amount, date):
        self.paymentID = paymentID
        self.billID = billID
        self.amount = amount
        self.date = date

     # CRUD operations for Payment
    def inserts(self) -> list[str]:
        query = "INSERT INTO Payment (paymentID, billID, amount, date) VALUES (%s, %s, %s, %s)"
        values = (payment.paymentID, payment.billID, payment.amount, payment.date)

    def updates(self) -> list[str]:
        query = "UPDATE Payment SET billID=%s, amount=%s, date=%s WHERE paymentID=%s"
        values = (payment.billID, payment.amount, payment.date, payment.paymentID)


class Reminder:
    def __init__(self, reminderID, calendarID):
        self.reminderID = reminderID
        self.calendarID = calendarID

class AppointmentReminder:
    def __init__(self, appointmentReminderID, appointmentID, reminderID):
        self.appointmentReminderID = appointmentReminderID
        self.appointmentID = appointmentID
        self.reminderID = reminderID

    # CRUD operations for AppointmentReminder
    def inserts(self) -> list[str]:
        query = "INSERT INTO AppointmentReminder (appointmentReminderID, appointmentID, reminderID) VALUES (%s, %s, %s)"
        values = (appointment_reminder.appointmentReminderID, appointment_reminder.appointmentID, appointment_reminder.reminderID)

    def updates(self) -> list[str]:
        query = "UPDATE AppointmentReminder SET appointmentID=%s, reminderID=%s WHERE appointmentReminderID=%s"
        values = (appointment_reminder.appointmentID, appointment_reminder.reminderID, appointment_reminder.appointmentReminderID)


class Message:
    def __init__(self, messageID, senderAccountID, recipientAccountID, messageText):
        self.messageID = messageID
        self.senderAccountID = senderAccountID
        self.recipientAccountID = recipientAccountID
        self.messageText = messageText

    # CRUD operations for Message
    def inserts(self) -> list[str]:
        query = "INSERT INTO Message (messageID, senderAccountID, recipientAccountID, messageText) VALUES (%s, %s, %s, %s)"
        values = (message.messageID, message.senderAccountID, message.recipientAccountID, message.messageText)

    def updates(self) -> list[str]:
        query = "UPDATE Message SET senderAccountID=%s, recipientAccountID=%s, messageText=%s WHERE messageID=%s"
        values = (message.senderAccountID, message.recipientAccountID, message.messageText, message.messageID)


class Fee:
    def __init__(self, feeID, reason, amount):
        self.feeID = feeID
        self.reason = reason
        self.amount = amount

    # CRUD operations for Fee
    def inserts(self) -> list[str]:
        query = "INSERT INTO Fee (feeID, reason, amount) VALUES (%s, %s, %s)"
        values = (fee.feeID, fee.reason, fee.amount)

    def updates(self) -> list[str]:
        query = "UPDATE Fee SET reason=%s, amount=%s WHERE feeID=%s"
        values = (fee.reason, fee.amount, fee.feeID)


class BillFee:
    def __init__(self, billID, feeID, insuranceID):
        self.billID = billID
        self.feeID = feeID
        self.insuranceID = insuranceID
    
    # CRUD operations for BillFee
    def inserts(self) -> list[str]:
        query = "INSERT INTO BillFee (billID, feeID, insuranceID) VALUES (%s, %s, %s)"
        values = (bill_fee.billID, bill_fee.feeID, bill_fee.insuranceID)

    def updates(self) -> list[str]:
        query = "UPDATE BillFee SET insuranceID=%s WHERE billID=%s AND feeID=%s"
        values = (bill_fee.insuranceID, bill_fee.billID, bill_fee.feeID)


class AppointmentSummary:
    def _int_(self, appointmentSummaryID, doctorAccountID, appointmentID, patientID):
        self.appointmentSummaryID = appointmentSummaryID
        self.doctorAccountID = doctorAccountID
        self.appointmentID = appointmentID
        self.patientID = patientID

    # CRUD operations for AppointmentSummary
    def inserts(self) -> list[str]:
        query = "INSERT INTO AppointmentSummary (appointmentSummaryID, doctorAccountID, appointmentID, patientID) VALUES (%s, %s, %s, %s)"
        values = (appointment_summary.appointmentSummaryID, appointment_summary.doctorAccountID, appointment_summary.appointmentID, appointment_summary.patientID)

    def updates(self) -> list[str]:
        query = "UPDATE AppointmentSummary SET doctorAccountID=%s, appointmentID=%s, patientID=%s WHERE appointmentSummaryID=%s"
        values = (appointment_summary.doctorAccountID, appointment_summary.appointmentID, appointment_summary.patientID, appointment_summary.appointmentSummaryID)


class MessageReminder:
    def _int_(self, messageReminderID, messageID, reminderID):
        self.messageReminderID = messageReminderID
        self.messageID = messageID
        self.reminderID = reminderID
