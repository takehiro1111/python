# append リストに要素を追加
l = [10,20,30]

l.append(40)
print(l)


# 複数の要素をリストへ追加
l.extend([50,60])
print(l)


# 指定したインデックスへ要素を追加
l.insert(0,100)
print(l)

# 要素を削除
  # 全ての要素を削除
# l.clear()
# print(l)

  # 特定の要素を削除
# l.remove(20)
# print(l)

  # 特定のインデックスを指定して要素を削除。変数に渡すまで。
# poped_item = l.pop(1) # インデックスを指定しない場合は末尾が自動的に指定される。
# print(poped_item)

del l[0] # delはpopのように変数に要素を渡せない。
print(l)


scores = [10, 20, 30, 20, 40]

print(len(scores))

print(min(scores))

print(max(scores))

print(sum(scores))

print(scores.count(10))

# 特定の要素がどのインデックスに入っているか。(最初の値しか使えない)
print(scores.index(20))

# 特定の要素がリストに存在するかどうか
print(10 in scores) # True
print(200 in scores) # False

# リストの要素を並び替える


scores = [10, 20, 30, 20, 40]

## 破壊的
#順序を逆にする
# scores.reverse()

# 要素を小さい順にソートする。
# scores.sort()
# # 要素を大きい順にソートする。
# scores.sort(reverse = True)

## 非破壊的
# 元データをそのままに要素を並び替える 
sorted_scores = sorted(scores,reverse = True)
print(sorted_scores)


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# スライス
# nums[2:5] = [200,300,400]

#nums[2:5] = [] # 値を指定しない場合は、指定した範囲の要素が削除される

# nums[:3] = []
nums[3:] = []
print(nums)


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# nums[2:5] = [100, 200, 300]

# sliced_list = nums[2:5]
# sliced_list = nums[2:8:2]
# sliced_list = nums[8:2:-2] #逆向きに後ろの要素から前の要素に向かって指定する
sliced_list = nums[::-1] # 要素を逆にするので、reverseメソッドの非破壊的版

print(nums)
print(sliced_list)
