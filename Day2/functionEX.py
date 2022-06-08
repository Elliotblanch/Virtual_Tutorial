def grade(name, homework, assessment, exam):
    total = homework + assessment + exam
    mark = total / 175 * 100
    if (mark > 80):
        return f"{name}: {mark}, A" 
    elif mark > 70: 
        return f"{name}: {mark} B"
    elif mark > 60:
        return f"{name}: {mark}, C" 
    elif mark > 50:
        return f"{name}: {mark}, D" 
    elif mark > 40:
        return f"{name}: {mark}, E"
    else: 
        return f"{name}: {mark}, fail"

name = input("Enter student's name: ")        
homework = int(input("Input homework marks /25: "))
assessment = int(input("Input assessment marks /50: "))
exam = int(input("Input exam marks /100: "))

print(grade(name, homework, assessment, exam))
