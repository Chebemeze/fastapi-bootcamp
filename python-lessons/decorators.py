""" decorators module contains practical use cases of
how decorators are used starting with manual decorators
and transitioning to using @

Examples:
    >>> from decorators
Manual usage:
    >>> make = timer_decorator(make_coffee)
    >>> print(make("Caffe"))
    Making Caffe...
    make_coffee took 0.0000s
    Here's your Caffe!
using @:
    >>> print(make("Caffe"))
    Making Caffe...
    make_coffee took 0.0000s
    Here's your Caffe!
"""

from functools import wraps

def timer_decorator(func):
    """ Calculates the time any function runs
    It receives the function as argument, calculates the time it took in running
    and returns the function

    Args:
        func: the name of the function it wants to modify

    Returns:
        str: what the function it calls returns

    Examples:
        >>> make = timer_decorator(make_coffee)
        >>> print(make("Caffe"))
        Making Caffe...
        make_coffee took 0.0000s
        Here's your Caffe!
    """
    @wraps(func)
    """reserves the metadata of the func passed"""
    def wrapper(*args, **kwargs):
        """ It receives args and kwargs passed to a function
        calls func passing the args and kwargs to it and returns the result

        Args:
            *args: It receives arguments passed to make_coffee in the form of a tupple
            **kwargs: If theres any key and value pair passed to make_coffe it receives it
        
        Returns:
            str: the name of the drink requested by the user
        """
        import time
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

# @timer_decorator
def make_coffee(drink_type):
    print(f"Making {drink_type}...")
    return f"Here's your {drink_type}!"

# Manually wrap the function
make = timer_decorator(make_coffee)
print(make("Caffe"))


#Another example using decorator @
def shout_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        print(f"\n{func.__name__}() is running ...")
        return result
    return wrapper

@shout_decorator
def greet(name):
    """Benz"""
    return f"Hello {name}"

print(greet.__name__)
print(greet.__doc__)


x = lambda a: a*a

print(x(2))

#writing a decorator function that will repeat another function
# Parameterized decorators
# def repeat(n):
#     def decorator_n(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             count = 0
#             result = []
#             while count < n:
#                 result.append(func(*args, **kwargs))
#                 count += 1
#             return result
#         return wrapper
#     return decorator_n

# @repeat(4)
# def make_food(food):
#     """This function returns the requested food"""
#     return f"{food} is ready."

# print(make_food("fried chicken"))
# print(make_food.__name__)

def repeat(n):
    """Decorator that repeats a function n times."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                print(f"Execution {i+1}/{n}")
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def make_coffee(drink_type):
    print(f"Making {drink_type}...")
    return f"☕ {drink_type}"

# Runs the function 3 times
results = make_coffee("Latte")
print(results)

import pytest
def test_calculate_subtotal_negative_raises_error():
    with pytest.raises(ValueError):
        calculate_subtotal(-5, 2)