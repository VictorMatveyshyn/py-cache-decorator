from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Any:

        key = ":".join([str(num) for num in args])
        key2 = ":".join([str(key) + ":" + str(val)
                         for key, val in kwargs.items()])
        key = key + ":" + key2
        answer = cache.get(key)
        if key not in cache:
            print("Calculating new result")
            answer = func(*args, **kwargs)
            cache[key] = answer
        else:
            print("Getting from cache")
        return answer
    return wrapper
