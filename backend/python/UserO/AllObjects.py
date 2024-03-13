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

    # Implement methods for CRUD operations (Create, Read, Update, Delete)

    def close(self):
        self.cursor.close()
        self.connection.close()

class PatientAccount:
    def __init__(self, accountID, age, ssn, chart, insurancePolicy, bills):
        self.accountID = accountID
        self.age = age
        self.ssn = ssn
        self.chart = chart
        self.insurancePolicy = insurancePolicy
        self.bills = bills

     def add_patient_account(self, patient):
        query = "INSERT INTO patient_accounts (accountID, age, ssn, chart, insurancePolicy, bills) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (patient.accountID, patient.age, patient.ssn, patient.chart, patient.insurancePolicy, patient.bills)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_patient_account_by_id(self, accountID):
        query = "SELECT * FROM patient_accounts WHERE accountID = %s"
        self.cursor.execute(query, (accountID,))
        result = self.cursor.fetchone()
        if result:
            accountID, age, ssn, chart, insurancePolicy, bills = result
            return PatientAccount(accountID, age, ssn, chart, insurancePolicy, bills)
        else:
            return None

    def update_patient_account(self, patient):
        query = "UPDATE patient_accounts SET age=%s, ssn=%s, chart=%s, insurancePolicy=%s, bills=%s WHERE accountID=%s"
        values = (patient.age, patient.ssn, patient.chart, patient.insurancePolicy, patient.bills, patient.accountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_patient_account(self, accountID):
        query = "DELETE FROM patient_accounts WHERE accountID = %s"
        self.cursor.execute(query, (accountID,))
        self.connection.commit()

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
    def add_chart(self, chart):
        query = "INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (chart.chartID, chart.weight, chart.height, chart.bloodPressure, chart.temperature, chart.prescriptions, chart.diagnoses, chart.allergies, chart.date)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_chart_by_id(self, chartID):
        query = "SELECT * FROM Chart WHERE chartID = %s"
        self.cursor.execute(query, (chartID,))
        result = self.cursor.fetchone()
        if result:
            chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date = result
            return Chart(chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date)
        else:
            return None

    def update_chart(self, chart):
        query = "UPDATE Chart SET weight=%s, height=%s, bloodPressure=%s, temperature=%s, prescriptions=%s, diagnoses=%s, allergies=%s, date=%s WHERE chartID=%s"
        values = (chart.weight, chart.height, chart.bloodPressure, chart.temperature, chart.prescriptions, chart.diagnoses, chart.allergies, chart.date, chart.chartID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_chart(self, chartID):
        query = "DELETE FROM Chart WHERE chartID = %s"
        self.cursor.execute(query, (chartID,))
        self.connection.commit()

class Prescription:
    def __init__(self, prescriptionID, drug, dosage, frequency, date, pharmacyID):
        self.prescriptionID = prescriptionID
        self.drug = drug
        self.dosage = dosage
        self.frequency = frequency
        self.date = date
        self.pharmacyID = pharmacyID

    # CRUD operations for Prescription
    def add_prescription(self, prescription):
        query = "INSERT INTO Prescription (prescriptionID, drug, dosage, frequency, date, pharmacyID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (prescription.prescriptionID, prescription.drug, prescription.dosage, prescription.frequency, prescription.date, prescription.pharmacyID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_prescription_by_id(self, prescriptionID):
        query = "SELECT * FROM Prescription WHERE prescriptionID = %s"
        self.cursor.execute(query, (prescriptionID,))
        result = self.cursor.fetchone()
        if result:
            prescriptionID, drug, dosage, frequency, date, pharmacyID = result
            return Prescription(prescriptionID, drug, dosage, frequency, date, pharmacyID)
        else:
            return None

    def update_prescription(self, prescription):
        query = "UPDATE Prescription SET drug=%s, dosage=%s, frequency=%s, date=%s, pharmacyID=%s WHERE prescriptionID=%s"
        values = (prescription.drug, prescription.dosage, prescription.frequency, prescription.date, prescription.pharmacyID, prescription.prescriptionID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_prescription(self, prescriptionID):
        query = "DELETE FROM Prescription WHERE prescriptionID = %s"
        self.cursor.execute(query, (prescriptionID,))
        self.connection.commit()

class InsurancePolicy:
    def __init__(self, insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount):
        self.insurancePolicyID = insurancePolicyID
        self.insuranceName = insuranceName
        self.insurancePolicyNumber = insurancePolicyNumber
        self.copayAmount = copayAmount

    # CRUD operations for InsurancePolicy
    def add_insurance_policy(self, insurance_policy):
        query = "INSERT INTO InsurancePolicy (insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount) VALUES (%s, %s, %s, %s)"
        values = (insurance_policy.insurancePolicyID, insurance_policy.insuranceName, insurance_policy.insurancePolicyNumber, insurance_policy.copayAmount)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_insurance_policy_by_id(self, insurancePolicyID):
        query = "SELECT * FROM InsurancePolicy WHERE insurancePolicyID = %s"
        self.cursor.execute(query, (insurancePolicyID,))
        result = self.cursor.fetchone()
        if result:
            insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount = result
            return InsurancePolicy(insurancePolicyID, insuranceName, insurancePolicyNumber, copayAmount)
        else:
            return None

    def update_insurance_policy(self, insurance_policy):
        query = "UPDATE InsurancePolicy SET insuranceName=%s, insurancePolicyNumber=%s, copayAmount=%s WHERE insurancePolicyID=%s"
        values = (insurance_policy.insuranceName, insurance_policy.insurancePolicyNumber, insurance_policy.copayAmount, insurance_policy.insurancePolicyID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_insurance_policy(self, insurancePolicyID):
        query = "DELETE FROM InsurancePolicy WHERE insurancePolicyID = %s"
        self.cursor.execute(query, (insurancePolicyID,))
        self.connection.commit()

class Pharmacy:
    def __init__(self, pharmacyID, name, address, phoneNumber):
        self.pharmacyID = pharmacyID
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    # CRUD operations for Pharmacy
    def add_pharmacy(self, pharmacy):
        query = "INSERT INTO Pharmacy (pharmacyID, name, address, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (pharmacy.pharmacyID, pharmacy.name, pharmacy.address, pharmacy.phoneNumber)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_pharmacy_by_id(self, pharmacyID):
        query = "SELECT * FROM Pharmacy WHERE pharmacyID = %s"
        self.cursor.execute(query, (pharmacyID,))
        result = self.cursor.fetchone()
        if result:
            pharmacyID, name, address, phoneNumber = result
            return Pharmacy(pharmacyID, name, address, phoneNumber)
        else:
            return None

    def update_pharmacy(self, pharmacy):
        query = "UPDATE Pharmacy SET name=%s, address=%s, phoneNumber=%s WHERE pharmacyID=%s"
        values = (pharmacy.name, pharmacy.address, pharmacy.phoneNumber, pharmacy.pharmacyID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_pharmacy(self, pharmacyID):
        query = "DELETE FROM Pharmacy WHERE pharmacyID = %s"
        self.cursor.execute(query, (pharmacyID,))
        self.connection.commit()

class StaffAccount:
    def __init__(self, staffAccountID, role, accountID):
        self.staffAccountID = staffAccountID
        self.role = role
        self.accountID = accountID

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


class Inbox:
    def __init__(self, inboxID, messages):
        self.inboxID = inboxID
        self.messages = messages

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

class Outbox:
    def __init__(self, outboxID, messages):
        self.outboxID = outboxID
        self.messages = messages

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

class Nurse:
    def __init__(self, nurseID, staffAccountID):
        self.nurseID = nurseID
        self.staffAccountID = staffAccountID

class Doctor:
    def __init__(self, doctorID, staffAccountID):
        self.doctorID = doctorID
        self.staffAccountID = staffAccountID

    # CRUD operations for Doctor
    def add_doctor(self, doctor):
        query = "INSERT INTO Doctor (doctorID, staffAccountID) VALUES (%s, %s)"
        values = (doctor.doctorID, doctor.staffAccountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_doctor_by_id(self, doctorID):
        query = "SELECT * FROM Doctor WHERE doctorID = %s"
        self.cursor.execute(query, (doctorID,))
        result = self.cursor.fetchone()
        if result:
            doctorID, staffAccountID = result
            return Doctor(doctorID, staffAccountID)
        else:
            return None

    def update_doctor(self, doctor):
        query = "UPDATE Doctor SET staffAccountID = %s WHERE doctorID = %s"
        values = (doctor.staffAccountID, doctor.doctorID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_doctor(self, doctorID):
        query = "DELETE FROM Doctor WHERE doctorID = %s"
        self.cursor.execute(query, (doctorID,))
        self.connection.commit()

class SysAdmin:
    def __init__(self, sysAdminID, staffAccountID):
        self.sysAdminID = sysAdminID
        self.staffAccountID = staffAccountID

    # CRUD operations for SysAdmin
    def add_sys_admin(self, sys_admin):
        query = "INSERT INTO SysAdmin (sysAdminID, staffAccountID) VALUES (%s, %s)"
        values = (sys_admin.sysAdminID, sys_admin.staffAccountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_sys_admin_by_id(self, sysAdminID):
        query = "SELECT * FROM SysAdmin WHERE sysAdminID = %s"
        self.cursor.execute(query, (sysAdminID,))
        result = self.cursor.fetchone()
        if result:
            sysAdminID, staffAccountID = result
            return SysAdmin(sysAdminID, staffAccountID)
        else:
            return None

    def update_sys_admin(self, sys_admin):
        query = "UPDATE SysAdmin SET staffAccountID = %s WHERE sysAdminID = %s"
        values = (sys_admin.staffAccountID, sys_admin.sysAdminID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_sys_admin(self, sysAdminID):
        query = "DELETE FROM SysAdmin WHERE sysAdminID = %s"
        self.cursor.execute(query, (sysAdminID,))
        self.connection.commit()

class Test:
    def __init__(self, testID, type, date, labID):
        self.testID = testID
        self.type = type
        self.date = date
        self.labID = labID

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

class TestResult:
    def __init__(self, testResultID, testID, date, result):
        self.testResultID = testResultID
        self.testID = testID
        self.date = date
        self.result = result

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

class Laboratory:
    def __init__(self, labID, name, address, phoneNumber):
        self.labID = labID
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    # CRUD operations for Laboratory
    def add_laboratory(self, laboratory):
        query = "INSERT INTO Laboratory (labID, name, address, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (laboratory.labID, laboratory.name, laboratory.address, laboratory.phoneNumber)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_laboratory_by_id(self, labID):
        query = "SELECT * FROM Laboratory WHERE labID = %s"
        self.cursor.execute(query, (labID,))
        result = self.cursor.fetchone()
        if result:
            labID, name, address, phoneNumber = result
            return Laboratory(labID, name, address, phoneNumber)
        else:
            return None

    def update_laboratory(self, laboratory):
        query = "UPDATE Laboratory SET name=%s, address=%s, phoneNumber=%s WHERE labID=%s"
        values = (laboratory.name, laboratory.address, laboratory.phoneNumber, laboratory.labID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_laboratory(self, labID):
        query = "DELETE FROM Laboratory WHERE labID = %s"
        self.cursor.execute(query, (labID,))
        self.connection.commit()

class Calendar:
    def __init__(self, calendarID):
        self.calendarID = calendarID

     # CRUD operations for Calendar
    def add_calendar(self, calendar):
        query = "INSERT INTO Calendar (calendarID) VALUES (%s)"
        values = (calendar.calendarID,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_calendar_by_id(self, calendarID):
        query = "SELECT * FROM Calendar WHERE calendarID = %s"
        self.cursor.execute(query, (calendarID,))
        result = self.cursor.fetchone()
        if result:
            calendarID = result[0]
            return Calendar(calendarID)
        else:
            return None

    def update_calendar(self, calendar):
        query = "UPDATE Calendar SET calendarID = %s WHERE calendarID = %s"
        values = (calendar.calendarID, calendar.calendarID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_calendar(self, calendarID):
        query = "DELETE FROM Calendar WHERE calendarID = %s"
        self.cursor.execute(query, (calendarID,))
        self.connection.commit()

class Appointment:
    def __init__(self, appointmentID, type, date, time, patientAccountID, doctorAccountID):
        self.appointmentID = appointmentID
        self.type = type
        self.date = date
        self.time = time
        self.patientAccountID = patientAccountID
        self.doctorAccountID = doctorAccountID

    # CRUD operations for Appointment
    def add_appointment(self, appointment):
        query = "INSERT INTO Appointment (appointmentID, doctorID, patientID, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (appointment.appointmentID, appointment.doctorID, appointment.patientID, appointment.date, appointment.time, appointment.status)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_appointment_by_id(self, appointmentID):
        query = "SELECT * FROM Appointment WHERE appointmentID = %s"
        self.cursor.execute(query, (appointmentID,))
        result = self.cursor.fetchone()
        if result:
            appointmentID, doctorID, patientID, date, time, status = result
            return Appointment(appointmentID, doctorID, patientID, date, time, status)
        else:
            return None

    def update_appointment(self, appointment):
        query = "UPDATE Appointment SET doctorID=%s, patientID=%s, date=%s, time=%s, status=%s WHERE appointmentID=%s"
        values = (appointment.doctorID, appointment.patientID, appointment.date, appointment.time, appointment.status, appointment.appointmentID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_appointment(self, appointmentID):
        query = "DELETE FROM Appointment WHERE appointmentID = %s"
        self.cursor.execute(query, (appointmentID,))
        self.connection.commit()

class Bill:
    def __init__(self, billID, amount, dateIssued, dueDate, patientAccountID):
        self.billID = billID
        self.amount = amount
        self.dateIssued = dateIssued
        self.dueDate = dueDate
        self.patientAccountID = patientAccountID

    # CRUD operations for Bill
    def add_bill(self, bill):
        query = "INSERT INTO Bill (billID, amount, dateIssued, dueDate, patientAccountID) VALUES (%s, %s, %s, %s, %s)"
        values = (bill.billID, bill.amount, bill.dateIssued, bill.dueDate, bill.patientAccountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_bill_by_id(self, billID):
        query = "SELECT * FROM Bill WHERE billID = %s"
        self.cursor.execute(query, (billID,))
        result = self.cursor.fetchone()
        if result:
            billID, amount, dateIssued, dueDate, patientAccountID = result
            return Bill(billID, amount, dateIssued, dueDate, patientAccountID)
        else:
            return None

    def update_bill(self, bill):
        query = "UPDATE Bill SET amount=%s, dateIssued=%s, dueDate=%s, patientAccountID=%s WHERE billID=%s"
        values = (bill.amount, bill.dateIssued, bill.dueDate, bill.patientAccountID, bill.billID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_bill(self, billID):
        query = "DELETE FROM Bill WHERE billID = %s"
        self.cursor.execute(query, (billID,))
        self.connection.commit()

class Payment:
    def __init__(self, paymentID, billID, amount, date):
        self.paymentID = paymentID
        self.billID = billID
        self.amount = amount
        self.date = date

     # CRUD operations for Payment
    def add_payment(self, payment):
        query = "INSERT INTO Payment (paymentID, billID, amount, date) VALUES (%s, %s, %s, %s)"
        values = (payment.paymentID, payment.billID, payment.amount, payment.date)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_payment_by_id(self, paymentID):
        query = "SELECT * FROM Payment WHERE paymentID = %s"
        self.cursor.execute(query, (paymentID,))
        result = self.cursor.fetchone()
        if result:
            paymentID, billID, amount, date = result
            return Payment(paymentID, billID, amount, date)
        else:
            return None

    def update_payment(self, payment):
        query = "UPDATE Payment SET billID=%s, amount=%s, date=%s WHERE paymentID=%s"
        values = (payment.billID, payment.amount, payment.date, payment.paymentID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_payment(self, paymentID):
        query = "DELETE FROM Payment WHERE paymentID = %s"
        self.cursor.execute(query, (paymentID,))
        self.connection.commit()

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
    def add_appointment_reminder(self, appointment_reminder):
        query = "INSERT INTO AppointmentReminder (appointmentReminderID, appointmentID, reminderID) VALUES (%s, %s, %s)"
        values = (appointment_reminder.appointmentReminderID, appointment_reminder.appointmentID, appointment_reminder.reminderID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_appointment_reminder_by_id(self, appointmentReminderID):
        query = "SELECT * FROM AppointmentReminder WHERE appointmentReminderID = %s"
        self.cursor.execute(query, (appointmentReminderID,))
        result = self.cursor.fetchone()
        if result:
            appointmentReminderID, appointmentID, reminderID = result
            return AppointmentReminder(appointmentReminderID, appointmentID, reminderID)
        else:
            return None

    def update_appointment_reminder(self, appointment_reminder):
        query = "UPDATE AppointmentReminder SET appointmentID=%s, reminderID=%s WHERE appointmentReminderID=%s"
        values = (appointment_reminder.appointmentID, appointment_reminder.reminderID, appointment_reminder.appointmentReminderID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_appointment_reminder(self, appointmentReminderID):
        query = "DELETE FROM AppointmentReminder WHERE appointmentReminderID = %s"
        self.cursor.execute(query, (appointmentReminderID,))
        self.connection.commit()

class Message:
    def __init__(self, messageID, senderAccountID, recipientAccountID, messageText):
        self.messageID = messageID
        self.senderAccountID = senderAccountID
        self.recipientAccountID = recipientAccountID
        self.messageText = messageText

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

class Fee:
    def __init__(self, feeID, reason, amount):
        self.feeID = feeID
        self.reason = reason
        self.amount = amount

    # CRUD operations for Fee
    def add_fee(self, fee):
        query = "INSERT INTO Fee (feeID, reason, amount) VALUES (%s, %s, %s)"
        values = (fee.feeID, fee.reason, fee.amount)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_fee_by_id(self, feeID):
        query = "SELECT * FROM Fee WHERE feeID = %s"
        self.cursor.execute(query, (feeID,))
        result = self.cursor.fetchone()
        if result:
            feeID, reason, amount = result
            return Fee(feeID, reason, amount)
        else:
            return None

    def update_fee(self, fee):
        query = "UPDATE Fee SET reason=%s, amount=%s WHERE feeID=%s"
        values = (fee.reason, fee.amount, fee.feeID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_fee(self, feeID):
        query = "DELETE FROM Fee WHERE feeID = %s"
        self.cursor.execute(query, (feeID,))
        self.connection.commit()

class BillFee:
    def __init__(self, billID, feeID, insuranceID):
        self.billID = billID
        self.feeID = feeID
        self.insuranceID = insuranceID
    
    # CRUD operations for BillFee
    def add_bill_fee(self, bill_fee):
        query = "INSERT INTO BillFee (billID, feeID, insuranceID) VALUES (%s, %s, %s)"
        values = (bill_fee.billID, bill_fee.feeID, bill_fee.insuranceID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_bill_fee_by_ids(self, billID, feeID):
        query = "SELECT * FROM BillFee WHERE billID = %s AND feeID = %s"
        self.cursor.execute(query, (billID, feeID))
        result = self.cursor.fetchone()
        if result:
            billID, feeID, insuranceID = result
            return BillFee(billID, feeID, insuranceID)
        else:
            return None

    def update_bill_fee(self, bill_fee):
        query = "UPDATE BillFee SET insuranceID=%s WHERE billID=%s AND feeID=%s"
        values = (bill_fee.insuranceID, bill_fee.billID, bill_fee.feeID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_bill_fee(self, billID, feeID):
        query = "DELETE FROM BillFee WHERE billID = %s AND feeID = %s"
        self.cursor.execute(query, (billID, feeID))
        self.connection.commit()

class AppointmentSummary:
    def _int_(self, appointmentSummaryID, doctorAccountID, appointmentID, patientID):
        self.appointmentSummaryID = appointmentSummaryID
        self.doctorAccountID = doctorAccountID
        self.appointmentID = appointmentsID
        self.patientID = patientID

    # CRUD operations for AppointmentSummary
    def add_appointment_summary(self, appointment_summary):
        query = "INSERT INTO AppointmentSummary (appointmentSummaryID, doctorAccountID, appointmentID, patientID) VALUES (%s, %s, %s, %s)"
        values = (appointment_summary.appointmentSummaryID, appointment_summary.doctorAccountID, appointment_summary.appointmentID, appointment_summary.patientID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_appointment_summary_by_id(self, appointmentSummaryID):
        query = "SELECT * FROM AppointmentSummary WHERE appointmentSummaryID = %s"
        self.cursor.execute(query, (appointmentSummaryID,))
        result = self.cursor.fetchone()
        if result:
            appointmentSummaryID, doctorAccountID, appointmentID, patientID = result
            return AppointmentSummary(appointmentSummaryID, doctorAccountID, appointmentID, patientID)
        else:
            return None

    def update_appointment_summary(self, appointment_summary):
        query = "UPDATE AppointmentSummary SET doctorAccountID=%s, appointmentID=%s, patientID=%s WHERE appointmentSummaryID=%s"
        values = (appointment_summary.doctorAccountID, appointment_summary.appointmentID, appointment_summary.patientID, appointment_summary.appointmentSummaryID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_appointment_summary(self, appointmentSummaryID):
        query = "DELETE FROM AppointmentSummary WHERE appointmentSummaryID = %s"
        self.cursor.execute(query, (appointmentSummaryID,))
        self.connection.commit()

class MessageReminder:
    def _int_(self, messageReminderID, messageID, reminderID):
        self.messageReminderID = messageReminderID
        self.messageID = messageID
        self.reminderID = reminderID
        
# Example usage
if __name__ == "__main__":