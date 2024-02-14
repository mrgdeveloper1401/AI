import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# print(mat.shape)

ar = np.arange(1, 100, 3)
# print(ar)
# print(ar.shape)

ar2 = np.arange(1, 60)
# print(ar2)
# print(ar2.shape)

ls = np.linspace(1, 10, 50)
print(ls)
print(ls.shape)
print(ls[1])
print(ls[1] - ls[0])
print(np.max(ls))
print(np.min(ls))
print(np.sum(ls))
