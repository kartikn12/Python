"""
In Python, decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code. 
"""

def decorator(func):
    def wrapper():
        print("Before calling function")
        func()
        print("Before calling function")
    return wrapper

@decorator
def greet():
    print("Hello word")
greet()

