from typing import Callable


def cache(func: Callable) -> Callable:
    cache1 = {}

    def wrapper(*args, **kwargs):

        key = ":".join([str(num) for num in args])

        answer = cache1.get(key)
        if answer is None:
            print("Calculating new result")
            answer = func(*args, **kwargs)
            cache1[key] = answer
        else:
            print("Getting from cache")
        return answer
    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
