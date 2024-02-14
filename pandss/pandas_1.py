import pandas as pd

# student table
student_info = {
    "name": ['mohammad', 'ali', 'reza'],
    'age': [20, 30, 40],
    'degree': ['a', 'b', 'c'],
}

student_df = pd.DataFrame(student_info)
print(student_df)
# print(student_df.info())

print('*' * 50)
print(student_df.head(2))
print('*' * 50)
print(student_df.tail(1))
