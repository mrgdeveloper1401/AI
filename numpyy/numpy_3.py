import numpy as nm
import numpy as np

v1 = np.random.rand(4)
# print(v1)
# print(v1.dtype)
# print(v1.shape)

v2 = np.random.random((4, 3))
# print(v2)

# print(v2[3])

# print(v2[2, 3])

v3 = np.random.randint(0, 251, 50)
# print(v3)
# print(v3.size)

v4 = np.random.randint(0, 9, 9).reshape(3, 3)
# print(v4)

v5 = np.arange(0, 12).reshape(4, 3)
# print(v5)


v6 = np.random.randint(0, 49, 49).reshape(7, 7)
# print("Original Matrix:")
# print(v6)
#
# np.random.shuffle(v6)
# print("\nShuffled Matrix:")
# print(v6)

v7 = np.random.normal(size=5)
# print(v7)

v8 = np.random.uniform()
# print(v8)

v9 = np.random.uniform(0, 10)
# print(v9)

v10 = np.random.uniform(0, 100, 6).reshape(3, 2)
# print(v10)


my_list = [1, 2, 3, 4, 5, 6, -1, -10, -20]
v11 = np.random.choice(my_list, size=6).reshape(3, 2)

binary_list = [0, 1]
v12 = np.random.choice(binary_list, size=(10, 10))
# print(v12)


