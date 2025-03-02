def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)  # 元の関数を呼び出す
        print(result)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper  # wrapper関数を返す

@log_decorator
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
