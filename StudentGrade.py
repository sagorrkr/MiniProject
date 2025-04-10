class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

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
    
    def calculate_average(self):
        if not self.grades:
            return 0
        else:
            return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        avg = self.calculate_average()
        return f"Name: {self.name}, Grades: {self.grades}, Agerage: {avg:.2f}"

    
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

    def add_grade(self, name, grade):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.add_grade(grade)
                return
            else:
                print(f"Student {name} not found. ")
    
