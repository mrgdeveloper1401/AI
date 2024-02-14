import pandas as pd
import numpy as np

s = np.random.randn(5)
# print(s.size)
# print(s)
p1 = pd.Series(s)
# print(p1)

# print(p1.axes)


p2 = pd.Series(s, index=['one', 'two', 'three', 'four', 'five'])
# print(p2)
# print(p2.axes)
# print(p2.dtype)
# print(p2.empty)
# print(p2.size)
# print(p2.values)
# print(p2.ndim)

np_1 = np.ones((5, 6))
# print(np_1)

p3 = pd.DataFrame(data=np_1, columns=['one', 'two', 'three', 'four', 'five', 'six'])
# print(p3)
# print(p3.axes)
# print(p3.tail(2))
# print(p3.head(2))
print(p3 > 1)


np_2 = np.zeros((3, 4))
# print(np_2)
# print(np_2.shape)





