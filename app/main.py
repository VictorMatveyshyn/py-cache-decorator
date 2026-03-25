from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache2 = {}

    def wrapper(*args, **kwargs) -> Any:

        key = ":".join([str(num) for num in args])
        answer = cache2.get(key)
        if answer is None:
            print("Calculating new result")
            answer = func(*args, **kwargs)
            cache2[key] = answer
        else:
            print("Getting from cache")
        return answer
    return wrapper
