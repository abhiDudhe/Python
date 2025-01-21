import logging

# Loggging to track the flow of the program wtih timeStamps
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Mylogs")
gen_log_file = logging.FileHandler('adminLog.log')
gen_log_file.setLevel(logging.DEBUG)
format_file = logging.Formatter("%(asctime)s : %(levelname)s --> %(message)s")
gen_log_file.setFormatter(format_file)
logger.addHandler(gen_log_file)

class Admin:
    logger.info("Inside the class")
    
    def __init__(self, adminId, adminName, studentId):
        logger.info("Initializing the class")
        print("Initializing the class")
        
        # Firstly checking the type of the input values
        try:
            if not isinstance(adminId, (int, str)):
                raise TypeError("AdminId must be an integer or string.")
            if not isinstance(adminName, str):
                raise TypeError("AdminName must be a string.")
            if not isinstance(studentId, (int, str)):
                raise TypeError("StudentId must be an integer or string.")
            
            self.adminId = str(adminId)
            self.adminName = adminName
            self.studentId = str(studentId)
            
            logger.info(f"AdminId is: {self.adminId}")
            logger.info(f"AdminName is: {self.adminName}")
            logger.info(f"StudentId is: {self.studentId}")
        except TypeError as te:
            logger.error(te)
            print(f"TypeError: {te}")
            return

        # If the input values are of correct type, then validating them
        self.validate_adminId()
        self.validate_adminName()
        self.validate_studentId()

    def validate_adminId(self):
        try:
            logger.debug("Starting validation for AdminId")
            if len(self.adminId) == 2 and self.adminId.isdigit():
                message = "Valid AdminId"
                logger.debug(message)
                logger.debug("passed validation for AdminId")
            else:
                raise ValueError("AdminId must be a 2-digit number.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_adminName(self):
        try:
            logger.debug("Starting validation for AdminName")
            if self.adminName.isalpha():
                message = "Valid AdminName"
                logger.debug(message)
                logger.debug("passed validation for AdminName")
            else:
                raise ValueError("AdminName must contain only alphabets.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_studentId(self):
        try:
            logger.debug("Starting validation for StudentId")
            if len(self.studentId) == 2 and self.studentId.isdigit():
                message = "Valid StudentId"
                logger.debug(message)
                logger.debug("passed validation for StudentId")
            else:
                raise ValueError("StudentId must be a 2-digit number.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")


# a=Admin(12, "Rahul", 12)

# b=Admin(12.5, "Rahul", 12)  

# c=Admin(12, 123, 12) 

# d=Admin(12, "Rahul", [12])  

# e=Admin(123, "Rahul", 12)  

f=Admin(12, "Rahul123", 12)  

# g=Admin(12, "Rahul", 123)  
