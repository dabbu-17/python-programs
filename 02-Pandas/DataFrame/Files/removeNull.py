import pandas as pd
#list the columns name
column_names = ['Student ID','Name','Age','Grade','Major','GPA','City']
#read the data from the csv file
data = pd.read_csv('02-Pandas\DataFrame\Files\student_data.csv', names= column_names, header=0)
#printing the nan values
print("Before Removing nan Values")
print(data.info())
#removing the nan values
data.dropna(inplace=True)
print("After Removing nan Values")
print(data.info())