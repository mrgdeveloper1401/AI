from numpy import array
from numpy.linalg import norm
from math import inf
from numpy import identity
from numpy.linalg import inv
from numpy import random

v = array(([1, 2, 3], [1, 2, 3]))
v1 = array([1, 2, 3])
v2 = array([2, 3, 4])

# print(v1 + v2)
# print(v2 - v1)
# print(v1 - v2)

mul_v = v1 * v2
# print(mul_v)

div_v = v1 / v2
# print(div_v)

# print(v1.dot(v2))

l1 = norm(v1, 1)
# print(l1)

l2 = norm(v1)
# print(l2)

norm_max = norm(v1, inf)
# print(norm_max)
# print(type(norm_max))

v3 = array(([1, 2, 3], [1, 2, 3]))
# print(v3)

v4 = array(([1, 2, 3], [1, 2, 3]))

mul_v3_v4 = v3 + v4
# print(mul_v3_v4)

v5 = array((
    [1, 2],
    [2, 3],
    [5, 6]
))

v6 = array((
    [1],
    [2]
))

# print(v5.dot(v6))

v7 = identity(3)
# print(v7)

v8 = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# try:
#     result = inv(v8)
#     print(result)
# except Exception as e:
#     print(f"Error: {e}")

x1 = random.randint(10, size=6)
x2 = random.randint(10, size=(3, 4))
x3 = random.randint(10, size=(3, 5, 5))

# print(x1)
# print(x2)
# print(x3)

# print(x1.size)
# print(x2.size)
# print(x3.size)

# print(x1.ndim)
# print(x2.ndim)
# print(x3.ndim)

# print(x1.itemsize)
# print(x2.itemsize)
# print(x3.itemsize)

# print(v8[0])

# print(v8[-1])

