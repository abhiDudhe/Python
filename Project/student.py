from asyncio.log import logger
import logging
import re
from datetime import datetime

genderList = ["male", "female", "other"]

class Student:
    def __init__(self, studentId, name, email, mobileNo, address, gender, dob, marks10th, marks12th):
        self.name = name.title() 
        
        valid_name = self.validate_name()
        if valid_name:
            log_file_name = f"{valid_name}.log"
        else:
            log_file_name = "default.log"

        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger("StudentLogger")
        gen_log_file = logging.FileHandler(log_file_name)
        gen_log_file.setLevel(logging.DEBUG)
        format_file = logging.Formatter("%(asctime)s : %(levelname)s --> %(message)s")
        gen_log_file.setFormatter(format_file)
        self.logger.addHandler(gen_log_file)

        self.logger.info("Initializing the Student class")

        try:
            if not isinstance(studentId, (int, str)):
                raise TypeError("Student ID must be an integer or string.")
            if not isinstance(email, str):
                raise TypeError("Email must be a string.")
            if not isinstance(mobileNo, (int, str)):
                raise TypeError("Mobile Number must be an integer or string.")
            if not isinstance(address, str):
                raise TypeError("Address must be a string.")
            if not isinstance(gender, str):
                raise TypeError("Gender must be a string.")
            if not isinstance(dob, str):
                raise TypeError("DOB must be a string (yyyy-mm-dd).")
            if not isinstance(marks10th, (int, float)):
                raise TypeError("10th Marks must be an integer or float.")
            if not isinstance(marks12th, (int, float)):
                raise TypeError("12th Marks must be an integer or float.")

            self.studentId = str(studentId)
            self.email = email.lower()
            self.mobileNo = str(mobileNo)
            self.address = address.title()
            self.gender = gender.lower()
            self.dob = dob
            self.marks10th = marks10th
            self.marks12th = marks12th

            self.logger.info(f"Student ID: {self.studentId}")
            self.logger.info(f"Name: {self.name}")
            self.logger.info(f"Email: {self.email}")
            self.logger.info(f"Mobile Number: {self.mobileNo}")
            self.logger.info(f"Address: {self.address}")
            self.logger.info(f"Gender: {self.gender}")
            self.logger.info(f"DOB: {self.dob}")
            self.logger.info(f"10th Marks: {self.marks10th}")
            self.logger.info(f"12th Marks: {self.marks12th}")

        except TypeError as te:
            self.logger.error(te)
            print(f"TypeError: {te}")
            return

        self.validate_studentId()
        self.validate_email()
        self.validate_mobileNo()
        self.validate_address()
        self.validate_gender()
        self.validate_dob()
        self.validate_marks10th()
        self.validate_marks12th()

    def validate_name(self):
        try:
            logger.debug("Validating Student Name")
            if self.name.isalpha():
                logger.debug("Validation passed for Student Name")
                return self.name
            else:
                raise ValueError("Student Name must contain only alphabets.")
        except ValueError as ve:
            print(f"ValueError: {ve}")
            return "invalid_name"

    def validate_studentId(self):
        try:
            self.logger.debug("Validating Student ID")
            if len(self.studentId) == 2 and self.studentId.isdigit():
                self.logger.debug("Validation passed for Student ID")
            else:
                raise ValueError("Student ID must be a 2-digit number.")
        except ValueError as ve:
            self.logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_email(self):
        try:
            self.logger.debug("Validating Email")
            email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(email_regex, self.email):
                self.logger.debug("Validation passed for Email")
            else:
                raise ValueError("Invalid Email. Please enter a valid Email address.")
        except ValueError as ve:
            self.logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_mobileNo(self):
        try:
            self.logger.debug("Validating Mobile Number")
            if len(self.mobileNo) == 10 and self.mobileNo.isdigit():
                self.logger.debug("Validation passed for Mobile Number")
            else:
                raise ValueError("Mobile Number must be a 10-digit number.")
        except ValueError as ve:
            self.logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_address(self):
        try:
            self.logger.debug("Validating Address")
            if self.address and any(char.isalpha() for char in self.address) and any(char.isdigit() for char in self.address):
                self.logger.debug("Validation passed for Address")
            else:
                raise ValueError("Address must contain both alphabets and numbers.")
        except ValueError as ve:
            self.logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_gender(self):
        try:
            self.logger.debug("Validating Gender")
            if self.gender in genderList:
                self.logger.debug("Validation passed for Gender")
            else:
                raise ValueError("Invalid Gender. Please enter a valid Gender.")
        except ValueError as ve:
            self.logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_dob(self):
        try:
            self.logger.debug("Validating DOB")
            dob_format = "%Y-%m-%d"
            dob_datetime = datetime.strptime(self.dob, dob_format)
            if dob_datetime > datetime.now():
                raise ValueError("DOB cannot be in the future.")
            self.logger.debug("Validation passed for DOB")
        except ValueError as ve:
            self.logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_marks10th(self):
        try:
            self.logger.debug("Validating 10th-grade Marks")
            if self.marks10th > 60:
                self.logger.debug("Validation passed for 10th-grade Marks")
            else:
                raise ValueError("10th-grade Marks should be greater than 60%.")
        except ValueError as ve:
            self.logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_marks12th(self):
        try:
            self.logger.debug("Validating 12th-grade Marks")
            if self.marks12th > 60:
                self.logger.debug("Validation passed for 12th-grade Marks")
            else:
                raise ValueError("12th-grade Marks should be greater than 60%.")
        except ValueError as ve:
            self.logger.critical(ve)
            print(f"ValueError: {ve}")


student = Student(
    studentId=12,
    name="John",
    email="john.doe@example.com",
    mobileNo="9876543210",
    address="123 Main Street",
    gender="male",
    dob="2000-05-15",
    marks10th=85.0,
    marks12th=90.5
)
student = Student(
    studentId=123,
    name="Abhi",
    email="john.doe@example.com",
    mobileNo="9876543210",
    address="123 Main Street",
    gender="male",
    dob="2000-05-15",
    marks10th=85.0,
    marks12th=90.5
)
