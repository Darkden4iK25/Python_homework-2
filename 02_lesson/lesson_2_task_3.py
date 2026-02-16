import math


def square(side):
    area = side * side
    return math.ceil(area)


print(square(4))     # 16
print(square(4.2))   # 18 (округлено вверх)