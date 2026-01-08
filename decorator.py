from functools import wraps
import time
import warnings


def mesure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function '{func.__name__}'" f"executed in {end-start:.6f} seconds")
        return result

    return wrapper


def mesure_execution_with_threshold_time(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            duration = end - start

            if duration > threshold:
                print(
                    f"the function '{func.__name__}'  executed in "
                    f"{duration:.6f} seconds (threshold = {threshold}s)"
                )
            else:
                print("executated more than threshold = {threshold}s")
            return result

        return wrapper

    return decorator


def deprecated(message=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warning_message = (
                message
                if message
                else f"Function '{func.__name__}' is deprecated,"
                f"it should not be used anymore"
            )

            warnings.warn(warning_message, category=DeprecationWarning, stacklevel=2)

            return func(*args, **kwargs)

        return wrapper

    return decorator


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


# Super!
