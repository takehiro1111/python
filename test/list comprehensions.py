prices = [100, 200, 150, 200, 100]

# prices_with_tax = []
# for price in prices:
#     prices_with_tax.append(price * 1.1)

prices_with_tax = [price * 1.1 for price in prices] # リスト内包表記

print(prices_with_tax)


# ifを用いた書き方
prices = [100, 200, 150, 200, 100]

# prices_with_tax = []
# for price in prices:
#     if price != 200:
#         prices_with_tax.append(price * 1.1)

prices_with_tax = [price * 1.1 for price in prices if price != 200]

print(prices_with_tax)


# リストから辞書を作成する
keys = ["math", "english", "physics"]
values = [62, 91, 84]

s = {key : value for key,value in zip(keys,values)}
print(s)

# リスト内包表記で書かない場合は以下の書き方になる。
# scores = {}
# # for item in zip(keys, values):
# #     # print(item)
# #     key, value = item
# #     # scores["math"] = 62
# #     scores[key] = value
# for key, value in zip(keys, values):
#     scores[key] = value


scores = [
  {"name": "Taro", "math": 70, "english": 82},
  {"name": "Jiro", "math": 67, "english": 61},
  {"name": "Saburo", "math": 81, "english": 58},
]

print("Name     Math     English")
print("-------- -------- --------")

for score in scores:
    # print(f'{score["name"]:8} {score["math"]:8} {score["english"]:8} ')
    for v in score.values():
        print(f'{v:8}', end = "")
        
    print() # print関数は、暗黙的に\nの性質を持っているためforとは切り離してバリュー単位ではなく辞書単位で最後に改行を入れたいためprint関数を用いている。

    