from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache1 = {}

    def wrapper(*args, **kwargs) -> Any:

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
