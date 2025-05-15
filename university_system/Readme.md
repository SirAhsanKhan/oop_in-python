## 📦 Project Features

- 🧑‍🎓 Create and manage student records
- 👩‍🏫 Add teacher profiles with salaries and subjects
- 📘 Enroll students in multiple courses
- 📝 Add and view student exam results (with validation)
- 🧠 Basic ID checking logic (e.g., student ID must start with `S`)
- 📂 Display full profiles for students and teachers

---

## 🧱 Code Structure

### 🔹 `Person` (Base Class)
- Shared attributes: `name`, `age`, `person_id`, `department`

### 🔹 `Student` (Inherits `Person`)
- Methods:
  - `enroll_course(course)`
  - `add_result(course, marks)`
  - `view_courses()`
  - `view_result()`
  - `show_info()`

### 🔹 `Teacher` (Inherits `Person`)
- Methods:
  - `show_info()`
  - `show_salary()`

---

## 🛠 How to Use (Sample)

```python
# Create a teacher
teacher1 = Teacher("Ahsan", 22, "T213", "400K", "Python", "CS")
teacher1.show_info()
teacher1.show_salary()

# Create a student
student1 = Students("Ahsan", "S2321", 17, "CS")
student1.enroll_course("Python")
student1.add_result("Python", 85)
student1.view_result()
student1.show_info()

