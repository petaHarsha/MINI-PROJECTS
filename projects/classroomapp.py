class student:
    def __init__(s,name,attendance,grades):
        s.name=name
        s.attendance=0
        s.grades=[]
    def mark_attendance(s):
        s.attendance+=1
        print(f"Attendance marked for {s.name}. Total attendance: {s.attendance}")
    def add_grade(s,grade):
        s.grades.append(grade)
        print(f"Added grade {grade} for {s.name}.")
    def view_report(s):
        avg_grade = sum(s.grades) / len(s.grades) if s.grades else 0
        print(f"Report for {s.name}:")
        print(f"Total Attendance: {s.attendance}")
        print(f"Grades: {s.grades}")
        print(f"Average Grade: {avg_grade:.2f}")
class ClassroomApp:
    def __init__(s):
        s.students=[]
    def add_student(s,name):
        s.students.append(student(name,0,[]))
        print(f"Added student: {name}")
    def mark_attendance(s,name):
        for stu in s.students:
            if stu.name==name:
                stu.mark_attendance()
                return
        print("Student not found.")
    def add_grade(s,name,grade):
        for stu in s.students:
            if stu.name==name:
                stu.add_grade(grade)
                return
        print("Student not found.")
    def view_reports(s):
        for stu in s.students:
            stu.view_report()
def main():
    app=ClassroomApp()
    while True:
        print("\n----- Classroom App -----")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Add Grade")
        print("4. View Reports")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter student name: ")
            app.add_student(name)
        elif choice==2:
            name=input("Enter student name to mark attendance: ")
            app.mark_attendance(name)
        elif choice==3:
            name=input("Enter student name to add grade: ")
            grade=float(input("Enter grade: "))
            app.add_grade(name,grade)
        elif choice==4:
            app.view_reports()
        elif choice==5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
