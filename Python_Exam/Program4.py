"""4. Student Grading System
- Write a program to calculate and display student grades.
- Input: Student&#39;s name and marks for 5 subjects.
- Output: Total marks, percentage, grade (A/B/C/Fail based on percentage)."""

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"
    
def student_grading_system():

    name = input("Enter the student's name: ")
    print("Enter the marks for 5 subjects (out of 100):")
    marks = []

    for i in range(1, 6):
        mark = float(input(f"Subject {i}: "))
        if 0 <= mark <= 100:
            marks.append(mark)
        else:
            print("Invalid marks entered. Please enter marks between 0 and 100.")
            return  
    total_marks = 0
    for mark in marks:
        total_marks += mark


    percentage = (total_marks / 500) * 100
    grade = calculate_grade(percentage)

    print(f"Name: {name}")
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

student_grading_system()
