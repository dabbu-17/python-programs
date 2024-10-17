'''
4.Write a python program and iterate the given tuples
Input:
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
'''
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
employees=[employee1, employee2, employee3]
for employee in employees:
    print(f"Name: {employee[0]}, ID: {employee[1]}, Department: {employee[2]}, Salary: {employee[3]}")