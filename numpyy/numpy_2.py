import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

v1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(v1.shape)

v2 = np.array([[1, 2, 3, 10],
               [4, 5, 6, 10],
               [7, 8, 9, 10]])

# print(v2.shape)
# print(v2.reshape(4, 3))
v3 = v2.reshape(4, 3)
# print(v3)

# print(v3.size)

# print(v3.dtype)
# print(v2.dtype)

# print(v2.itemsize)

# print(v2 > 2)

# print(np.sum(v2 > 5))
# print(v2 > 5)
# print(np.sum(v2))

v4 = np.zeros([10, 10])
# print(v4)

v5 = np.ones([10, 10])
# print(v5)