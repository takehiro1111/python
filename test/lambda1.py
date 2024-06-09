a = [1, 2, 3]
result = map(lambda x: x ** 2, a)
print(list(result))  # [1, 4, 9]


# lambdaの元になる書き方は以下である。
# def x_map(x):
#   return x ** 2

# l = [1, 2, 3]
# no_lambda = map(x_map,l)

# print(list(no_lambda))
