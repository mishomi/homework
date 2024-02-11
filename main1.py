class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
    def addCourse(self, course):
        self.courses.append(course)
        print(f"{self.name} was registered for the course {course}.")
    def displayCourses(self):
        print(f"{self.name}'s registered courses: ")
        for i in self.courses:
            print(i)
student1 = Student("misho", 101)
student2 = Student("mihsa", 102)

student1.addCourse("java")
student1.addCourse("python")
student2.addCourse("ocaml")

student1.displayCourses()
student2.displayCourses()
