class Student:
    def __init__(self,name):
        self.name = name
        self.grade = []

    def add_grade(self, grade):
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                self.grade.append(grade)
                print(f"Added grade {grade} for {self.name}")
            else: 
                print("Grade must be between 0 to 100")
        except ValueError:
            print("Invalid Grade! Please enter a number ")

    
class GradeTracker:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                print(f"{name} is already in the tracker. ")
                return
        new_student = Student(name)
        self.students.append(new_student)
        print(f"Student Added: {name}")