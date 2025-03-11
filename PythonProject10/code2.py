def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=5)
def greet(name):
    print(f"Hello {name}")

@repeat(num_times=3)
def suma(x,y):
    print("a")
    return x+y


greet("World")
w = suma(4,5)