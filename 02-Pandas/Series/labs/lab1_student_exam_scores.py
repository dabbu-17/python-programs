# Lab 1: Student Exam Scores Analysis

import pandas as pd

# Input data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Create a Pandas Series with student names as index and exam scores as values
student_scores = pd.Series(data=exam_scores, index=students, name='Exam Scores')

# Display the Series
print("Lab 1: Student Exam Scores")
print(student_scores)

# ... (rest of the code remains the same)
