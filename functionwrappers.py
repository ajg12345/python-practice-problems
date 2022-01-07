from time import sleep, time
from functools import wraps

# Explanation video here:
# https://www.youtube.com/watch?v=gIVRaAb-XzA
# seems like the syntax for this decorator is the same, and all wraps does is
# protect the funcname and docstring for test harnesses
# a complex example
def timer(func):
    # This function shows the execution time of
    # the function object passed
    @wraps(func)
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r}  executed in {(t2-t1):.4f}s")
        return result

    return wrap_func


def retry(retry_amounts):
    """
    retries function up to retry amounts, and rests an increasing amount of time each failure.
    """

    def wrap(func):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            retries = 0
            while retries < retry_amounts:
                try:
                    result = func(*args, **kwargs)
                    print("successful")
                    return result
                except Exception as e:
                    retries = retries + 1
                    print(str(e))
                    print("failed")
                    sleep(retries)
            print("execution aborted")
            return

        return wrap_func

    return wrap


@timer
def taketime(x: int) -> None:
    sleep(x)


taketime(3)
