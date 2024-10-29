import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie','David'],
    'Age': [24, 30, 22,21],
    'Grade': ['A', 'B', 'A','A']
}

df = pd.DataFrame(data)
print(df)
