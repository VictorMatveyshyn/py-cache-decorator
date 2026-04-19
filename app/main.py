from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        # key = ":".join([str(num) for num in args])
        # key2 = ":".join([str(key) + ":" + str(val)
        #                  for key, val in kwargs.items()])
        # key = key + ":" + key2
        key = args, tuple(sorted(kwargs.items()))
        if key not in cache:
            print("Calculating new result")
            cache[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache.get(key)
    return wrapper

@cache
def long_time_func(a: int, b: int, c =1) -> int:

    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

long_time_func(1, 2, c=3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
