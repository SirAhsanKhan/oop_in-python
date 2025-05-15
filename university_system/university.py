class Person :
    def __init__(self, name , age, person_id, department):
        self.name = name
        self.person_id = person_id
        self.age = age
        self.department = department

class Teacher(Person):
    def __init__(self, name, age, person_id, salary, subject, department):
        if not str(person_id).startswith("T"):
            raise ValueError("Invalid Teacher ID. It must start with 'T'.")
        
        super().__init__(name, age, person_id, department)
        self.__salary = salary
        self.subject = subject

    

    def show_info(self):
        print(f"Teacher ID: {self.person_id}\n"
                f"Teacher Name: {self.name}\n"
                f"Teacher Age: {self.age}\n"
                f"Department: {self.department}\n"
                f"Subject: {self.subject}")
        
    def get_salary(self):
        return self.__salary


class Students(Person):
    def __init__(self, name, age ,person_id, department):
        if not str(person_id).startswith("S"):
            raise ValueError("Invalid student ID. Must start with 'S'")

        super().__init__(name, person_id , age , department)
        self.courses = []
        self.result = {}
       
    def show_info(self):
        print(f"Student ID: {self.person_id}\n"
                f"Student Name: {self.name}\n"
                f"Student Age: {self.age}\n"
                f"Department: {self.department}\n"
                f"Courses Enrolled: {', '.join(self.courses) if self.courses else 'None'}\n"
                f"Results: {self.result}")
    
    def enroll_course(self, courses):
        self.courses.append(courses)

        print(f"Congrats you are enrolled in course ''{courses}''")

    def view_courses(self):
        if self.courses:
            print(f"You are enrolled in {self.courses}")
        else:
            print("You are not enrolled in any courses yet.")

    def add_result(self, course, marks ):

        if course in self.courses:
         self.result[course] = marks
         print(f"Result added : {course} : {marks} marks")
            
        else :
            print(f"You must enroll in ``{course}`` first")

    def view_result(self):
        if self.result:
            print(self.result)
        else:
            print("Make sure to add result first")


#Teachher testing
teacher1 = Teacher("Ahsan",22,"T213","400K","Python","CS")
#showing collective info
teacher1.show_info()
#shows only salary because its private
print("Your Monthly Salary: "+ teacher1.get_salary())


#student testing
# store basic info
student1 = Students("Ahsan", 17,"S123", "CS")
#enroll in new Course
student1.enroll_course("Python")
student1.enroll_course("Maths")
# Adding result of respective courses
student1.add_result("Python", 85)
student1.add_result("Maths", 85)
#shows only result
student1.view_result()
#showing collective info
student1.show_info()
        
        