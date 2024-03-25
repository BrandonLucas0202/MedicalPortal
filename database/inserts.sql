--Patient Account
INSERT INTO PatientAccount (accountID, age, ssn, chart, insurancePolicy, bills)
VALUES 
('account-1', 28, '123-45-6781', 'chart-1', 'insurance-1', 'bill-1');

INSERT INTO PatientAccount (accountID, age, ssn, chart, insurancePolicy, bills)
VALUES 
('account-2', 45, '123-45-6782', 'chart-2', 'insurance-2', 'bill-2');

INSERT INTO PatientAccount (accountID, age, ssn, chart, insurancePolicy, bills)
VALUES 
('account-3', 37, '123-45-6783', 'chart-3', 'insurance-3', 'bill-3');

INSERT INTO PatientAccount (accountID, age, ssn, chart, insurancePolicy, bills)
VALUES 
('account-4', 50, '123-45-6784', 'chart-4', 'insurance-4', 'bill-4');

INSERT INTO PatientAccount (accountID, age, ssn, chart, insurancePolicy, bills)
VALUES 
('account-5', 32, '123-45-6785', 'chart-5', 'insurance-5', 'bill-5');

--Chart
INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date)
VALUES 
('account-1', 70, 175, '120/80', 36.6, 'Prescription A', 'Diagnosis A', 'Allergy A', '2024-03-25');

INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date)
VALUES 
('account-2', 80, 180, '130/85', 36.7, 'Prescription B', 'Diagnosis B', 'Allergy B', '2024-03-25');

INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date)
VALUES 
('account-3', 65, 170, '115/75', 36.5, 'Prescription C', 'Diagnosis C', 'Allergy C', '2024-03-25');

INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date)
VALUES 
('account-4', 90, 185, '140/90', 36.9, 'Prescription D', 'Diagnosis D', 'Allergy D', '2024-03-25');

INSERT INTO Chart (chartID, weight, height, bloodPressure, temperature, prescriptions, diagnoses, allergies, date)
VALUES 
('account-5', 75, 178, '125/80', 36.8, 'Prescription E', 'Diagnosis E', 'Allergy E', '2024-03-25');
