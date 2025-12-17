import numpy as np

# Data:Marks of 5 Students (Maths, Science, English)
# Rows = Students, Columns = Subjects
marks = np.array([
    [45, 80, 75],  # Student A
    [90, 88, 92],  # Student B
    [32, 40, 35],  # Student C 
    [60, 65, 60],  # Student D
    [25, 30, 28]   # Student E 
])

print("--- Student Exam Analysis ---")

# 1. Calculate Total Marks for each student
total_marks = np.sum(marks, axis=1)
print("Total Marks of each student:", total_marks)

# 2. Calculate Average Marks of the class (Mean)
class_avg = np.mean(marks)
print(f"Class Average Score: {class_avg:.2f}")

# 3. Find who passed? (Passing criteria: Total > 150)
passed_students = total_marks > 150
print("Did Student Pass? (True/False):", passed_students)

# 4. Count how many passed
count_pass = np.sum(passed_students)
print(f"Total Students Passed: {count_pass} out of 5")