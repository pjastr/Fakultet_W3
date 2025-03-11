import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funkcja {func.__name__} wykonana w {end_time - start_time} sekund.")
        return result
    return wrapper

@timer
def long_running_function():
    for _ in range(1000000):
        pass

long_running_function()