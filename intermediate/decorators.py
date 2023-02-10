import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        result  = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

@start_end_decorator
def print_name():
    print("jhon")


@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)


def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num=5)
def greet(name):
    print(f'hello {name}')
    
greet("Jhon")