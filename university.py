class Students:
    def __init__(self, student_name, student_id, student_age, department,result):

        self.student_name = student_name
        self.student_age = student_age
        self.student_id = student_id
        self.department = department
        self.courses = []
        self.result = {}
       
    def Show_info(self):
        return  (f"Student ID: {self.student_id}\n"
                f"Student Name: {self.student_name}\n"
                f"Student Age: {self.student_age}\n"
                f"Department: {self.department}\n"
                f"Courses Enrolled: {', '.join(self.courses) if self.courses else 'None'}")
    
    def Enroll_course(self, courses):
        self.courses.append(courses)

        print(f"Congrats you are enrolled in course ''{courses}''")

    def View_Courses(self):
        if self.courses:
            print(f"You are enrolled in {self.courses}")
        else:
            print("You are not enrolled in any courses yet.")

    



student1 = Students("Ahsan",2321,17,"CS")


student1.View_Courses()
# print(student1.Show_info())
        
        