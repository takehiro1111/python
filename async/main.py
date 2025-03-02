# import asyncio

# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(10)  # 非同期で2秒間待機
#     print("Task 1 completed")

# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(3)  # 非同期で2秒間待機
#     print("Task 2 completed")

# async def main():
#     await asyncio.gather(task1(), task2())  # task1とtask2を同時に実行

# asyncio.run(main())

import asyncio

async def task1():
    await asyncio.sleep(5)
    print("Task 1 started")
    await asyncio.sleep(10)
    return "タスク1の結果"

async def task2():
    print("Task 2 started")
    await asyncio.sleep(5)
    return "タスク2の結果"

async def main():
    # 複数のタスクを同時に実行し、両方の結果を待つ
    results = await asyncio.gather(task1(), task2())
    
    # resultsはタスクの結果のリスト
    print(results)  # ['タスク1の結果', 'タスク2の結果']
    
    # 個別の結果にアクセスする場合
    result1, result2 = results
    print(result1)  # タスク1の結果
    print(result2)  # タスク2の結果

asyncio.run(main())
