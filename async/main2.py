import asyncio
import random

# 数字を2倍にする関数
async def double_number(number):
    print(f"{number}を2倍にします")
    # 実際のAPIリクエストやDB操作がここにある想定
    await asyncio.sleep(8)  # APIリクエストの時間を模擬
    result = number * 2
    print(f"{number}の2倍は{result}です")
    return result

# 数字に10を足す関数
async def add_ten(number):
    print(f"{number}に10を足します")
    # 別のAPI操作を想定
    await asyncio.sleep(2)  # 別のAPI操作の時間
    result = number + 10
    print(f"{number}+10は{result}です")
    return result

async def main():
    # まず数字を2倍にして、その結果に10を足す
    # number = 5
    # doubled = await double_number(number)  # 5を2倍→10
    # final = await add_ten(doubled)         # 10+10→20
    # print(f"最終結果: {final}")  # 20

    # もし2つの操作が独立している場合は並行実行できる
    print("\n独立した操作を並行実行:")
    results = await asyncio.gather(
        double_number(7),  # 7を2倍
        add_ten(3)         # 3に10を足す
    )
    print(f"並行実行の結果: {results}")  # [14, 13]

asyncio.run(main())
