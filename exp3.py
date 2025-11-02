-- Patient Dimension
CREATE TABLE DimPatient (
    PatientKey INT PRIMARY KEY AUTO_INCREMENT,
    PatientID VARCHAR(10),
    PatientName VARCHAR(100),
    Gender VARCHAR(10),
    Age INT,
    City VARCHAR(50)
);

-- Doctor Dimension
CREATE TABLE DimDoctor (
    DoctorKey INT PRIMARY KEY AUTO_INCREMENT,
    DoctorID VARCHAR(10),
    DoctorName VARCHAR(100),
    Specialization VARCHAR(50),
    Department VARCHAR(50)
);

-- Date Dimension
CREATE TABLE DimDate (
    DateKey INT PRIMARY KEY AUTO_INCREMENT,
    FullDate DATE,
    Day INT,
    Month INT,
    Year INT
);

-- Treatment Fact Table
CREATE TABLE FactTreatment (
    TreatmentKey INT PRIMARY KEY AUTO_INCREMENT,
    PatientKey INT,
    DoctorKey INT,
    DateKey INT,
    Diagnosis VARCHAR(100),
    TreatmentCost DECIMAL(10,2),
    FOREIGN KEY (PatientKey) REFERENCES DimPatient(PatientKey),
    FOREIGN KEY (DoctorKey) REFERENCES DimDoctor(DoctorKey),
    FOREIGN KEY (DateKey) REFERENCES DimDate(DateKey)
);

INSERT INTO DimPatient (PatientID, PatientName, Gender, Age, City)
VALUES 
('P001', 'Rahul Sharma', 'Male', 34, 'Mumbai'),
('P002', 'Sneha Patil', 'Female', 28, 'Pune'),
('P003', 'Arjun Mehta', 'Male', 45, 'Delhi');

INSERT INTO DimDoctor (DoctorID, DoctorName, Specialization, Department)
VALUES 
('D001', 'Dr. Kavita Rao', 'Cardiology', 'Heart Care'),
('D002', 'Dr. Ajay Kumar', 'Orthopedics', 'Bone Care'),
('D003', 'Dr. Neha Joshi', 'Neurology', 'Brain Care');

INSERT INTO DimDate (FullDate, Day, Month, Year)
VALUES 
('2025-01-12', 12, 1, 2025),
('2025-02-05', 5, 2, 2025),
('2025-03-20', 20, 3, 2025);

INSERT INTO FactTreatment (PatientKey, DoctorKey, DateKey, Diagnosis, TreatmentCost)
VALUES
(1, 1, 1, 'Heart Checkup', 3500.00),
(2, 2, 2, 'Fracture Treatment', 5000.00),
(3, 3, 3, 'Migraine Therapy', 4200.00);

SELECT 
    p.PatientName,
    d.DoctorName,
    dt.FullDate,
    f.Diagnosis,
    f.TreatmentCost
FROM FactTreatment f
JOIN DimPatient p ON f.PatientKey = p.PatientKey
JOIN DimDoctor d ON f.DoctorKey = d.DoctorKey
JOIN DimDate dt ON f.DateKey = dt.DateKey;


--slice
SELECT 
    p.PatientName,
    d.DoctorName,
    dt.FullDate,
    f.Diagnosis,
    f.TreatmentCost
FROM FactTreatment f
JOIN DimPatient p ON f.PatientKey = p.PatientKey
JOIN DimDoctor d ON f.DoctorKey = d.DoctorKey
JOIN DimDate dt ON f.DateKey = dt.DateKey
WHERE dt.Month = 2 AND dt.Year = 2025;


--dice
SELECT 
    p.PatientName,
    d.DoctorName,
    d.Specialization,
    p.City,
    f.Diagnosis,
    f.TreatmentCost
FROM FactTreatment f
JOIN DimPatient p ON f.PatientKey = p.PatientKey
JOIN DimDoctor d ON f.DoctorKey = d.DoctorKey
JOIN DimDate dt ON f.DateKey = dt.DateKey
WHERE d.Specialization = 'Cardiology' AND p.City = 'Mumbai';

--drill down
--yearlevel
SELECT 
    dt.Year,
    SUM(f.TreatmentCost) AS TotalCost
FROM FactTreatment f
JOIN DimDate dt ON f.DateKey = dt.DateKey
GROUP BY dt.Year;

--Drill down to month-level:
SELECT 
    dt.Year,
    dt.Month,
    SUM(f.TreatmentCost) AS TotalCost
FROM FactTreatment f
JOIN DimDate dt ON f.DateKey = dt.DateKey
GROUP BY dt.Year, dt.Month
ORDER BY dt.Year, dt.Month;

--roll up
SELECT 
    dt.Year,
    SUM(f.TreatmentCost) AS YearlyTotal
FROM FactTreatment f
JOIN DimDate dt ON f.DateKey = dt.DateKey
GROUP BY dt.Year;


--pivot
SELECT 
    d.DoctorName,
    SUM(CASE WHEN p.City = 'Mumbai' THEN f.TreatmentCost ELSE 0 END) AS Mumbai,
    SUM(CASE WHEN p.City = 'Pune' THEN f.TreatmentCost ELSE 0 END) AS Pune,
    SUM(CASE WHEN p.City = 'Delhi' THEN f.TreatmentCost ELSE 0 END) AS Delhi
FROM FactTreatment f
JOIN DimPatient p ON f.PatientKey = p.PatientKey
JOIN DimDoctor d ON f.DoctorKey = d.DoctorKey
GROUP BY d.DoctorName;

