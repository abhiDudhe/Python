import logging

# Loggging to track the flow of the program wtih timeStamps
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Mylogs")
gen_log_file = logging.FileHandler('coursesLog.log')
gen_log_file.setLevel(logging.DEBUG)
format_file = logging.Formatter("%(asctime)s : %(levelname)s --> %(message)s")
gen_log_file.setFormatter(format_file)
logger.addHandler(gen_log_file)

courseLists = [
    'Computer Engineering', 
    'Electronics Engineering', 
    'Mechanical Engineering', 
    'Civil Engineering',
    'Information Technology'
]

class Courses:
    logger.info("Inside the class")
    
    def __init__(self, courseId, courseName, adminId):
        logger.info("Initializing the Courses class")
        print("Initializing the Courses class")
        
        # Firstly checking the type of the input values
        try:
            if not isinstance(courseId, (int, str)):
                raise TypeError("CourseId must be an integer or string.")
            if not isinstance(courseName, str):
                raise TypeError("CourseName must be a string.")
            if not isinstance(adminId, (int, str)):
                raise TypeError("AdminId must be an integer or string.")

            self.courseId = str(courseId)
            self.courseName = courseName.title()
            self.adminId = str(adminId)
            
            logger.info(f"CourseId is: {self.courseId}")
            logger.info(f"CourseName is: {self.courseName}")
            logger.info(f"AdminId is: {self.adminId}")
        
        except TypeError as te:
            logger.error(te)
            print(f"TypeError: {te}")
            return
        
        # If the input values are of correct type, then validating them
        self.validate_courseId()
        self.validate_courseName()
        self.validate_adminId()

    def validate_courseId(self):
        try:
            logger.debug("Starting validation for CourseId")
            if len(self.courseId) == 2 and self.courseId.isdigit():
                message = "Valid CourseId"
                logger.debug(message)
                logger.debug("Validation passed for CourseId")
            else:
                raise ValueError("CourseId must be a 2-digit number.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_courseName(self):
        try:
            logger.debug("Starting validation for CourseName")
            if self.courseName in courseLists:
                message = "Valid CourseName"
                logger.debug(message)
                logger.debug("Validation passed for CourseName")
            else:
                raise ValueError("Invalid CourseName. Please enter a valid course name.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")

    def validate_adminId(self):
        try:
            logger.debug("Starting validation for AdminId")
            if len(self.adminId) == 2 and self.adminId.isdigit():
                message = "Valid AdminId"
                logger.debug(message)
                logger.debug("Validation passed for AdminId")
            else:
                raise ValueError("AdminId must be a 2-digit number.")
        except ValueError as ve:
            logger.critical(ve)
            print(f"ValueError: {ve}")


a = Courses(12, "computer enring", 12)

# b = Courses(12, "Computer Engineering", 12)

# c = Courses(123, "Computer Engineering", 12)

# d = Courses(12, "Computer Engineering", 123)

# e = Courses([12], "Computer Engineering", 12)
