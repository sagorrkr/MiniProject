class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                self.grades.append(grade)
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
        return f"Name: {self.name}, Grades: {self.grades}, Average: {avg:.2f}"

    
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
        
        print(f"Student {name} not found. ")
    
    def display_all(self):
        if not self.students:
            print(f"No students in the tracker.")
        else:
            print("Student grade summery")
            for student in self.students:
                print(student)

def main():
    tracker = GradeTracker()

    while True:
        print("\nGrade Tracker Menu")
        print("1. Add a student")
        print("2. Add a grade")
        print("3. Display all students")
        print("4. Exit")

        choice = input("Enter your choice(1-4)")

        if choice == "1":
                name = input("Enter student name: ")
                tracker.add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            grade = input("Enter grade (0-100): ")
            tracker.add_grade(name, grade)

        elif choice == "3":
            tracker.display_all()

        elif choice == "4":
            print("Goodbye! Final summary:")
            tracker.display_all()
            break

        else:
            print("Invalid choice. Please try again (1-4).")


if __name__ == "__main__":
    main()