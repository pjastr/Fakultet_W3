def my_decorator(func):
    def wrapper():
        print("Coś jest wykonywane przed funkcją.")
        func()
        print("Coś jest wykonywane po funkcji.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()