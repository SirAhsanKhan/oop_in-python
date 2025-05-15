class Students:
    def __init__(self, student_name, student_id, student_age, department):

        self.student_name = student_name
        self.student_age = student_age
        self.student_id = student_id
        self.department = department
        self.courses = []
        self.result = {}
       
    def Show_info(self):
        print(f"Student ID: {self.student_id}\n"
                f"Student Name: {self.student_name}\n"
                f"Student Age: {self.student_age}\n"
                f"Department: {self.department}\n"
                f"Courses Enrolled: {', '.join(self.courses) if self.courses else 'None'}\n"
                f"Results: {self.result}")
    
    def Enroll_course(self, courses):
        self.courses.append(courses)

        print(f"Congrats you are enrolled in course ''{courses}''")

    def View_Courses(self):
        if self.courses:
            print(f"You are enrolled in {self.courses}")
        else:
            print("You are not enrolled in any courses yet.")

    def Add_result(self, course, marks ):

        if course in self.courses:
         self.result[course] = marks
         print(f"Result added : {course} : {marks} marks")
            
        else :
            print(f"You must enroll in ``{course}`` first")

    def View_result(self):
        if self.result:
            print(self.result)
        else :
            print("Make sure to add result first")


# store basic info
student1 = Students("Ahsan", 2321, 17, "CS")
#enroll in new Course
student1.Enroll_course("Python")
student1.Enroll_course("Maths")
# Adding result of respective courses
student1.Add_result("Python", 85)
student1.Add_result("Maths", 85)
#shows only result
student1.View_result()
#showing collective info
student1.Show_info()
        
        