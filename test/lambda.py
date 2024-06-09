# 関数名(実引数) → 処理の結果
# 関数名 → 処理の内容 → 変数への代入、関数の引数

# def double(n):
#     return n * 2

# def triple(n):
#     return n * 3

def calc(n, func):
    # return double(10)
    return func(n)

# print(calc(10, double))
print(calc(10, lambda n: n * 2)) # 無名関数
print(calc(10, lambda n: n * 3))
                    # 仮引数:関数内の処理
