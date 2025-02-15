create database employeeDb

drop database employeeDb



create database employeeDb;
USE EmployeeDB;

CREATE TABLE Employees (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255),
    mobile NVARCHAR(15),
    address NVARCHAR(MAX),
    salary DECIMAL(10,2)
);

CREATE TABLE LeaveRequests_Temp (
    id INT IDENTITY(1,1) PRIMARY KEY,
    emp_id INT,
    leave_date DATE,
    status NVARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (emp_id) REFERENCES Employees(id)
);


CREATE TABLE LeaveRequests (
    id INT IDENTITY(1,1) PRIMARY KEY,
    emp_id INT,
    leave_date DATE,
    status NVARCHAR(20) DEFAULT 'Approved',
    FOREIGN KEY (emp_id) REFERENCES Employees(id)
);

select * from Employees

select * from LeaveRequests

select * from LeaveRequests_Temp