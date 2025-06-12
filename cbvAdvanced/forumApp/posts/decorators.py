import time


def measure_execution_time(func):
    def wrapper(request, *args, **kwargs):
        start_time = time.time()
        response = func(request, *args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"The view executed in {execution_time}s")

        return response
    return wrapper
