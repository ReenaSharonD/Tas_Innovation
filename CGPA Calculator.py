import tkinter as tk
from tkinter import messagebox

def calculate_cgpa():
    total_credit_hours = 0
    total_weighted_grade_points = 0

    num_subjects = int(entry_subjects.get())

    for _ in range(num_subjects):
        grade = entry_grades[_].get()
        credit_hours = int(entry_credit_hours[_].get())

        if grade == "A+":
            grade_point = 4.0
        elif grade == "A":
            grade_point = 3.7
        elif grade == "B+":
            grade_point = 3.3
        elif grade == "B":
            grade_point = 3.0
        elif grade == "C+":
            grade_point = 2.3
        elif grade == "C":
            grade_point = 2.0
        elif grade == "D":
            grade_point = 1.0
        else:
            grade_point = 0.0

        weighted_grade_points = grade_point * credit_hours
        total_weighted_grade_points += weighted_grade_points
        total_credit_hours += credit_hours

    cgpa = total_weighted_grade_points / total_credit_hours
    messagebox.showinfo("CGPA Calculation", f"Your CGPA is: {cgpa:.2f}")

root = tk.Tk()
root.title("CGPA Calculator")

label_subjects = tk.Label(root, text="Enter the number of subjects:")
label_subjects.pack()

entry_subjects = tk.Entry(root)
entry_subjects.pack()

entry_grades = []
entry_credit_hours = []

for i in range(5):  
    frame = tk.Frame(root)
    frame.pack()

    label_grade = tk.Label(frame, text=f"Subject {i+1} Grade:")
    label_grade.pack(side="left")

    entry_grade = tk.Entry(frame)
    entry_grade.pack(side="left")
    entry_grades.append(entry_grade)

    label_credit_hours = tk.Label(frame, text="Credit Hours:")
    label_credit_hours.pack(side="left")

    entry_credit_hour = tk.Entry(frame)
    entry_credit_hour.pack(side="left")
    entry_credit_hours.append(entry_credit_hour)

calculate_button = tk.Button(root, text="Calculate CGPA", command=calculate_cgpa)
calculate_button.pack()

root.mainloop()
