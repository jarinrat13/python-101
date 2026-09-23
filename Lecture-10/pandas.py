<<<<<<< HEAD
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

average_age = df['Age'].mean()
print("\nAverahe Age:", average_age)

filtered_df = df[df['Age'] > 28]
print("\nFiltered dataFrame (Age > 25):\n", filtered_df)

df['Salary'] = [50000, 60000, 70000]
=======
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

average_age = df['Age'].mean()
print("\nAverahe Age:", average_age)

filtered_df = df[df['Age'] > 28]
print("\nFiltered dataFrame (Age > 25):\n", filtered_df)

df['Salary'] = [50000, 60000, 70000]
>>>>>>> 36e2367c506c94705546caf13817ba0e32d9cbfa
print("\nDataFrame with Salary colum:\n", df)