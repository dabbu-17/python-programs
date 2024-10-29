''' create a dataFrame with student info , such as student_id , name , gender , technology and batch.
 write this dataFrame to csv file , the dataFrame created should contain 5 students details. '''
import pandas as pd
data = {
    'student_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['F', 'M', 'M', 'M', 'F'],
    'technology': ['Python', 'Java', 'Python', 'Java', 'Python'],
    'batch': ['A', 'B', 'A', 'B', 'A']
}
df = pd.DataFrame(data)
csv_file_path = '02-Pandas/DataFrame/Files/student_info.csv'
df.to_csv(csv_file_path, index=False)
print(f'Data has been written to {csv_file_path}')

