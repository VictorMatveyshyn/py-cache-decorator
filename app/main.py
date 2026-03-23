from typing import Callable





def cache(func: Callable) -> Callable:
    cache1 = {}
    def wrapper(*args, **kwargs):
        key = f"{args[0]}:{args[1]}:{args[2]}"
        answer = cache1.get(key)
        if answer is None:
            answer = (args[0] ** args[1] ** args[2]) % (args[0] * args[2])
            cache1[key] = answer
        return answer
    return wrapper

`