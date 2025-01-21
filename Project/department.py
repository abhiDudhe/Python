import logging

# Loggging to track the flow of the program wtih timeStamps
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Mylogs")
gen_log_file = logging.FileHandler('departmentLog.log')
gen_log_file.setLevel(logging.DEBUG)
format_file = logging.Formatter("%(asctime)s : %(levelname)s --> %(message)s")
gen_log_file.setFormatter(format_file)
logger.addHandler(gen_log_file)


departmentLists = [
    'Computer Engineering', 
    'Electronics Engineering', 
    'Mechanical Engineering', 
    'Civil Engineering', 
    'Information Technology'
]
isSeatAvailable = ("Yes", "No")

class Department:
    logger.info("Inside the Department class")
    
    def __init__(self, deptId, departmentName, allocatedSeat, courseId):
        logger.info("Initializing the Department class")
        print("Initializing the Department class")
        
        # Firstly checking the type of the input values

        try:
            if not isinstance(deptId, (int, str)):
                raise TypeError("Department Id must be an integer or string.")
            if not isinstance(departmentName, str):
                raise TypeError("Department Name must be a string.")
            if not isinstance(allocatedSeat, str):
                raise TypeError("Allocated Seat must be a string.")
            if not isinstance(courseId, (int, str)):
                raise TypeError("Course Id must be an integer or string.")

            self.deptId = str(deptId)
            self.departmentName = departmentName.title()
            self.allocatedSeat = allocatedSeat.title()
            self.courseId = str(courseId)
            
            logger.info(f"Department Id is: {self.deptId}")
            logger.info(f"Department Name is: {self.departmentName}")
            logger.info(f"Allocated Seat is: {self.allocatedSeat}")
            logger.info(f"Course Id is: {self.courseId}")

        except TypeError as te:
            logger.error(te)
            print(f"TypeError: {te}")
            return
        
        # If the input values are of correct type, then validating them
        self.validate_deptId()
        self.validate_departmentName()
        self.validate_allocatedSeat()
        self.validate_courseId()

    def validate_deptId(self):
        try:
            logger.debug("Starting validation for Department Id")
            if len(self.deptId) == 2 and self.deptId.isdigit():
                message = "Valid Department Id"
                logger.debug(message)
                logger.debug("Validation passed for Department Id")
            else:
                raise ValueError("Department Id must be a 2-digit number.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_departmentName(self):
        try:
            logger.debug("Starting validation for Department Name")
            if self.departmentName in departmentLists:
                message = "Valid Department Name"
                logger.debug(message)
                logger.debug("Validation passed for Department Name")
            else:
                raise ValueError("Invalid Department Name. Please enter a valid department name.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_allocatedSeat(self):
        try:
            logger.debug("Starting validation for Allocated Seat")
            if self.allocatedSeat in isSeatAvailable:
                message = "Valid Allocated Seat"
                logger.debug(message)
                logger.debug("Validation passed for Allocated Seat")
            else:
                raise ValueError("Allocated Seat must be 'Yes' or 'No'.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_courseId(self):
        try:
            logger.debug("Starting validation for Course Id")
            if len(self.courseId) == 2 and self.courseId.isdigit():
                message = "Valid Course Id"
                logger.debug(message)
                logger.debug("Validation passed for Course Id")
            else:
                raise ValueError("Course Id must be a 2-digit number.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")



a = Department(12, "computer enring", "yes", 12)


# b = Department(12, "Computer Engineering", "Yes", 12)


# c = Department(123, "Computer Engineering", "Yes", 12)

# d = Department(12, "Computer Engineering", "Maybe", 12)


# e = Department(12, "Computer Engineering", "Yes", 123)


# f = Department([12], "Computer Engineering", "Yes", 12)
