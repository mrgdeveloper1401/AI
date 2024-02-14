import pandas as pd

p1 = pd.Series()
# print(p1)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p2 = pd.Series(data)
# print(p2)

data_2 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
p3 = pd.Series(data_2)
# print(p3)

data_3 = {
    "name": ['mohammad', 'ali', 'reza', 'someday', 'fatemeh'],
    'rate': [0.1, 0.2, 0.3, 0.4, 0.5]
}
p4 = pd.Series(data_3)
# print(p4)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p5 = pd.Series(number, index=range(1000, 1009))
# print(p5)

data_4 = {
    'a': 1,
    'b': 2
}
p6 = pd.Series(data_4, index=['a', 'b', 'c'])
# print(p6)


data_5 = {

}


