import time
from functools import wraps
#decoraters
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[Log] method {func.__name__}() executed successfully")
        return result
    return wrapper
def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        role = kwargs.pop("role", "user")  # safely remove role
        if role != "admin":
            print("Access Denied, Only Admin has the access right")
            return None
        return func(*args, **kwargs)  # original function unchanged
    return wrapper
def performance_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start=time.time()
        result = func(*args, **kwargs)
        end=time.time()
        print(f"Execution time:{end-start:6f} seconds")
        return result
    return wrapper


