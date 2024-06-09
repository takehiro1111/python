# タプル
# in, len(), index(), count() ... → 使える
# append(), insert(), pop() ... → 使えない
# 要素を変更できない。

# tokyo = ("JPY", 36, 140)
tokyo = "JPY", 36, 140

tokyo = list(tokyo)
# tokyo[0] = "YEN"
tokyo = tuple(tokyo)

print(tokyo)
print(tokyo[0])



# タプルのアンパック(要素を変数化する事)
tokyo = ("JPY", 36, 140)

# # currency, lat, long = tokyo
# _, lat, long = tokyo
# # print(currency)
# print(lat)
# print(long)

# currency, *location = tokyo
currency, *_ = tokyo
print(currency)
# print(location)
