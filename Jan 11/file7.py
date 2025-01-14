import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}


data = pd.DataFrame(data)

data.to_excel('Book1.xlsx',index=0)