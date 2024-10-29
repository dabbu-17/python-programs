import pandas as pd

data = {
    'student_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female']
}

df = pd.DataFrame(data)
print(df)
