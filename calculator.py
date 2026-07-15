# grades.py
# A simple student grade calculator
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"
int marks = int(input("enter your marks"))
print("Marks:", marks)
print("Grade:", calculate_grade(marks))