USE MedPortal;
-- PatientAccount table
CREATE TABLE PatientAccount (
  accountID VARCHAR(36) NOT NULL,
  age INT,
  ssn VARCHAR(20),
  chart VARCHAR(36),
  insurancePolicy VARCHAR(36),
  bills VARCHAR(36),
  PRIMARY KEY (accountID)
);

-- Chart table
CREATE TABLE Chart (
  chartID VARCHAR(36) NOT NULL,
  weight FLOAT,
  height FLOAT,
  bloodPressure VARCHAR(20),
  temperature FLOAT,
  prescriptions TEXT,
  diagnoses TEXT,
  allergies TEXT,
  date DATE,
  PRIMARY KEY (chartID),
  FOREIGN KEY (chartID) REFERENCES PatientAccount(accountID)
);

-- Prescription table
CREATE TABLE Prescription (
  prescriptionID VARCHAR(36) NOT NULL,
  drug VARCHAR(255),
  dosage VARCHAR(255),
  frequency VARCHAR(255),
  date DATE,
  pharmacyID VARCHAR(36),
  PRIMARY KEY (prescriptionID)
);

-- InsurancePolicy table
CREATE TABLE InsurancePolicy (
  insurancePolicyID VARCHAR(36) NOT NULL,
  insuranceName VARCHAR(255),
  insurancePolicyNumber VARCHAR(255),
  copayAmount FLOAT,
  PRIMARY KEY (insurancePolicyID)
);

-- Pharmacy table
CREATE TABLE Pharmacy (
  pharmacyID VARCHAR(36) NOT NULL,
  name VARCHAR(255),
  address TEXT,
  phoneNumber VARCHAR(20),
  PRIMARY KEY (pharmacyID)
);

-- StaffAccount table
CREATE TABLE StaffAccount (
  staffAccountID VARCHAR(36) NOT NULL,
  role VARCHAR(20) NOT NULL,
  accountID VARCHAR(36),
  PRIMARY KEY (staffAccountID),
  FOREIGN KEY (accountID) REFERENCES Account(accountID),
  CHECK (role IN ('Nurse', 'Doctor', 'SysAdmin', 'Clinical Staff'))
);


-- Account table
CREATE TABLE Account (
  accountID VARCHAR(36) NOT NULL,
  email VARCHAR(255),
  phoneNumber VARCHAR(20),
  address TEXT,
  calendarID VARCHAR(36),
  inboxID VARCHAR(36),
  outboxID VARCHAR(36),
  PRIMARY KEY (accountID)
);

-- Inbox table
CREATE TABLE Inbox (
  inboxID VARCHAR(36) NOT NULL,
  messages TEXT,
  PRIMARY KEY (inboxID)
);

-- Outbox table
CREATE TABLE Outbox (
  outboxID VARCHAR(36) NOT NULL,
  messages TEXT,
  PRIMARY KEY (outboxID)
);

-- Nurse table
CREATE TABLE Nurse (
  nurseID VARCHAR(36) NOT NULL,
  staffAccountID VARCHAR(36),
  PRIMARY KEY (nurseID),
  FOREIGN KEY (staffAccountID) REFERENCES StaffAccount(staffAccountID)
);

-- Doctor table
CREATE TABLE Doctor (
  doctorID VARCHAR(36) NOT NULL,
  staffAccountID VARCHAR(36),
  PRIMARY KEY (doctorID),
  FOREIGN KEY (staffAccountID) REFERENCES StaffAccount(staffAccountID)
);

-- SysAdmin table
CREATE TABLE SysAdmin (
  sysAdminID VARCHAR(36) NOT NULL,
  staffAccountID VARCHAR(36),
  PRIMARY KEY (sysAdminID),
  FOREIGN KEY (staffAccountID) REFERENCES StaffAccount(staffAccountID)
);

-- Test table
CREATE TABLE Test (
  testID VARCHAR(36) NOT NULL,
  type VARCHAR(20) NOT NULL,
  date DATE,
  labID VARCHAR(36),
  PRIMARY KEY (testID),
  CHECK (type IN ('BloodTest', 'XRay', 'MRI', 'Other'))
);


-- TestResult table
CREATE TABLE TestResult (
  testResultID VARCHAR(36) NOT NULL,
  testID VARCHAR(36),
  date DATE,
  result TEXT,
  PRIMARY KEY (testResultID),
  FOREIGN KEY (testID) REFERENCES Test(testID)
);

-- Laboratory table
CREATE TABLE Laboratory (
  labID VARCHAR(36) NOT NULL,
  name VARCHAR(255),
  address TEXT,
  phoneNumber VARCHAR(20),
  PRIMARY KEY (labID)
);

-- Calendar table
CREATE TABLE Calendar (
  calendarID VARCHAR(36) NOT NULL,
  PRIMARY KEY (calendarID)
);

-- Appointment table
CREATE TABLE Appointment (
  appointmentID VARCHAR(36) NOT NULL,
  type VARCHAR(20) NOT NULL,
  date DATE,
  time TIME,
  patientAccountID VARCHAR(36),
  doctorAccountID VARCHAR(36),
  PRIMARY KEY (appointmentID),
  FOREIGN KEY (patientAccountID) REFERENCES PatientAccount(accountID),
  FOREIGN KEY (doctorAccountID) REFERENCES StaffAccount(staffAccountID),
  CHECK (type IN ('Consultation', 'FollowUp', 'Emergency'))
);


-- Bill table
CREATE TABLE Bill (
  billID VARCHAR(36) NOT NULL,
  amount FLOAT,
  dateIssued DATE,
  dueDate DATE,
  patientAccountID VARCHAR(36),
  PRIMARY KEY (billID),
  FOREIGN KEY (patientAccountID) REFERENCES PatientAccount(accountID)
);

-- Payment table
CREATE TABLE Payment (
  paymentID VARCHAR(36) NOT NULL,
  billID VARCHAR(36),
  amount FLOAT,
  date DATE,
  PRIMARY KEY (paymentID),
  FOREIGN KEY (billID) REFERENCES Bill(billID)
);

-- Reminder table
CREATE TABLE Reminder (
  reminderID VARCHAR(36) NOT NULL,
  calendarID VARCHAR(36),
  PRIMARY KEY (reminderID),
  FOREIGN KEY (calendarID) REFERENCES Calendar(calendarID)
);

-- AppointmentReminder table
CREATE TABLE AppointmentReminder (
  appointmentReminderID VARCHAR(36) NOT NULL,
  appointmentID VARCHAR(36),
  reminderID VARCHAR(36),
  PRIMARY KEY (appointmentReminderID),
  FOREIGN KEY (appointmentID) REFERENCES Appointment(appointmentID),
  FOREIGN KEY (reminderID) REFERENCES Reminder(reminderID)
);

-- Message table
CREATE TABLE Message (
  messageID VARCHAR(36) NOT NULL,
  senderAccountID VARCHAR(36),
  recipientAccountID VARCHAR(36),
  messageText TEXT,
  PRIMARY KEY (messageID),
  FOREIGN KEY (senderAccountID) REFERENCES Account(accountID),
  FOREIGN KEY (recipientAccountID) REFERENCES Account(accountID)
);

-- Fee table
CREATE TABLE Fee (
  feeID VARCHAR(36) NOT NULL,
  reason TEXT,
  amount FLOAT,
  PRIMARY KEY (feeID)
);

-- BillFee (association between Bill and Fee)
CREATE TABLE BillFee (
  billID VARCHAR(36) NOT NULL,
  feeID VARCHAR(36) NOT NULL,
  PRIMARY KEY (billID, feeID),
  FOREIGN KEY (billID) REFERENCES Bill(billID),
  FOREIGN KEY (feeID) REFERENCES Fee(feeID)
);
