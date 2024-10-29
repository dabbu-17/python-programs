import pandas as pd
csv_file_path = '02-Pandas\DataFrame\Files\customer_data.csv'
df = pd.read_csv(csv_file_path)
print(df.describe().T)

