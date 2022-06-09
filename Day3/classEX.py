class Student:
    def __init__(self, name="Student", age="Student", cohort="Student"):
        self.name = name
        self.age = age
        self.cohort = cohort

    

    def grade(self, homework, assessment, exam):

        total = homework + assessment + exam
        mark = total / 175 * 100
        if (mark > 80):
         return f"{self.name}: {mark}, A" 
        elif mark > 70: 
            return f"{self.name}: {mark} B"
        elif mark > 60:
            return f"{self.name}: {mark}, C" 
        elif mark > 50:
            return f"{self.name}: {mark}, D" 
        elif mark > 40:
            return f"{self.name}: {mark}, E"
        else: 
            return f"{self.name}: {mark}, fail"

student1 = Student("Dan", 22, "3-A")

print(student1.grade(23, 32, 55))