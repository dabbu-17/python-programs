#import pandas
import pandas as pd
#list the columns name
column_names = ['Student ID','Name','Age','Grade','Major','GPA','City']
#read the data from the csv file
data = pd.read_csv('02-Pandas\DataFrame\Files\student_data.csv', names= column_names, header=0)
#Find the duplicate values
duplicate_rows = data.duplicated()
#Printing the no of duplicate rows
print("Number of duplicate rows:", duplicate_rows)
