-- Account table
CREATE TABLE Account (
  accountID VARCHAR(36) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phoneNumber VARCHAR(20) NOT NULL,
  address TEXT NOT NULL,
  PRIMARY KEY (accountID)
);

-- InsurancePolicy table
CREATE TABLE InsurancePolicy (
  insurancePolicyID VARCHAR(36) NOT NULL,
  insuranceName VARCHAR(255) NOT NULL,
  insurancePolicyNumber VARCHAR(255) NOT NULL,
  copayAmount FLOAT NOT NULL,
  PRIMARY KEY (insurancePolicyID)
);

-- PatientAccount table
CREATE TABLE PatientAccount (
  patientAccountID VARCHAR(36) NOT NULL,
  age INT NOT NULL,
  ssn VARCHAR(20) NOT NULL,
  insurancePolicyID VARCHAR(36) NOT NULL,
  PRIMARY KEY (patientAccountID),
  FOREIGN KEY (patientAccountID) REFERENCES Account(accountID),
  FOREIGN KEY (insurancePolicyID) REFERENCES InsurancePolicy(insurancePolicyID)
);

-- Chart table
CREATE TABLE Chart (
  chartID VARCHAR(36) NOT NULL,
  weight FLOAT NOT NULL,
  height FLOAT NOT NULL,
  bloodPressure VARCHAR(20) NOT NULL,
  temperature FLOAT NOT NULL,
  diagnoses TEXT NOT NULL,
  allergies TEXT NOT NULL,
  date DATE NOT NULL,
  patientAccountID VARCHAR(36) NOT NULL,
  PRIMARY KEY (chartID),
  FOREIGN KEY (patientAccountID) REFERENCES PatientAccount(patientAccountID)
);

-- Pharmacy table
CREATE TABLE Pharmacy (
  pharmacyID VARCHAR(36) NOT NULL,
  name VARCHAR(255) NOT NULL,
  address TEXT NOT NULL,
  phoneNumber VARCHAR(20),
  PRIMARY KEY (pharmacyID)
);

-- Prescription table
CREATE TABLE Prescription (
  prescriptionID VARCHAR(36) NOT NULL,
  drug VARCHAR(255) NOT NULL,
  dosage VARCHAR(255) NOT NULL,
  frequency VARCHAR(255) NOT NULL,
  date DATE NOT NULL,
  pharmacyID VARCHAR(36) NOT NULL,
  patientAccountID VARCHAR(36) NOT NULL,
  PRIMARY KEY (prescriptionID),
  FOREIGN KEY (pharmacyID) REFERENCES Pharmacy(pharmacyID),
  FOREIGN KEY (patientAccountID) REFERENCES PatientAccount(patientAccountID)
);

-- StaffAccount table
CREATE TABLE StaffAccount (
  staffAccountID VARCHAR(36) NOT NULL,
  role VARCHAR(20) NOT NULL,
  accountID VARCHAR(36) NOT NULL,
  PRIMARY KEY (staffAccountID),
  FOREIGN KEY (accountID) REFERENCES Account(accountID),
  CHECK (role IN ('Nurse', 'Doctor', 'Admin', 'Staff'))
);

-- HashedPassword table
CREATE TABLE HashedPassword (
  email VARCHAR(255) NOT NULL,
  hash VARCHAR(255) NOT NULL,
  accountID VARCHAR(36),
  PRIMARY KEY (email, hash),
  FOREIGN KEY (accountID) REFERENCES Account(accountID)
);

-- Test table
CREATE TABLE Test (
  testID VARCHAR(36) NOT NULL,
  description TEXT NOT NULL,
  date DATE NOT NULL,
  labID VARCHAR(36) NOT NULL,
  patientAccountID VARCHAR(36) NOT NULL,
  PRIMARY KEY (testID),
  FOREIGN KEY (patientAccountID) REFERENCES PatientAccount(patientAccountID)
);

-- TestResult table
CREATE TABLE TestResult (
  testResultID VARCHAR(36) NOT NULL,
  testID VARCHAR(36) NOT NULL,
  date DATE NOT NULL,
  result TEXT NOT NULL,
  PRIMARY KEY (testResultID),
  FOREIGN KEY (testID) REFERENCES Test(testID)
);

-- Laboratory table
CREATE TABLE Laboratory (
  labID VARCHAR(36) NOT NULL,
  name VARCHAR(255) NOT NULL,
  address TEXT NOT NULL,
  phoneNumber VARCHAR(20) NOT NULL,
  PRIMARY KEY (labID)
);

-- Appointment table
CREATE TABLE Appointment (
  appointmentID VARCHAR(36) NOT NULL,
  description TEXT NOT NULL,
  date DATE NOT NULL,
  time TIME NOT NULL,
  patientAccountID VARCHAR(36) NOT NULL,
  doctorAccountID VARCHAR(36) NOT NULL,
  PRIMARY KEY (appointmentID),
  FOREIGN KEY (patientAccountID) REFERENCES PatientAccount(patientAccountID),
  FOREIGN KEY (doctorAccountID) REFERENCES StaffAccount(staffAccountID)
);

-- Bill table
CREATE TABLE Bill (
  billID VARCHAR(36) NOT NULL,
  description TEXT NOT NULL,
  amount FLOAT NOT NULL,
  dateIssued DATE NOT NULL,
  dueDate DATE NOT NULL,
  patientAccountID VARCHAR(36) NOT NULL,
  PRIMARY KEY (billID),
  FOREIGN KEY (patientAccountID) REFERENCES PatientAccount(patientAccountID)
);

-- Payment table
CREATE TABLE Payment (
  paymentID VARCHAR(36) NOT NULL,
  billID VARCHAR(36) NOT NULL,
  amount FLOAT NOT NULL,
  date DATE NOT NULL,
  PRIMARY KEY (paymentID),
  FOREIGN KEY (billID) REFERENCES Bill(billID)
);

-- Reminder table
CREATE TABLE Reminder (
  reminderID VARCHAR(36) NOT NULL,
  description TEXT NOT NULL,
  date DATE NOT NULL,
  time TIME NOT NULL,
  accountID VARCHAR(36) NOT NULL,
  PRIMARY KEY (reminderID),
  FOREIGN KEY (accountID) REFERENCES Account(accountID)
);

-- Message table
CREATE TABLE Message (
  messageID VARCHAR(36) NOT NULL,
  date DATE NOT NULL,
  time TIME NOT NULL,
  messageText TEXT NOT NULL,
  senderAccountID VARCHAR(36) NOT NULL,
  recipientAccountID VARCHAR(36) NOT NULL,
  PRIMARY KEY (messageID),
  FOREIGN KEY (senderAccountID) REFERENCES Account(accountID),
  FOREIGN KEY (recipientAccountID) REFERENCES Account(accountID)
);
