a = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, a)
print(list(result))  # [2, 4, 6]


# def x_map(x):
#   return x % 2 == 0

# a = [1, 2, 3, 4, 5, 6]
# l = filter(x_map,a)

# print(list(l))
