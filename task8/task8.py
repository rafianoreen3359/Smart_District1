""" Task: 

● API Middleware Simulator: A backend team needs reusable function wrappers that 
handle execution timing, input/output logging, and role-based access control — without 
touching the original functions. All wrappers must be stackable and all activity must go 
through the `logging` module, not print."""
import logging
import time
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        logging.info("Execution time: %.4f seconds", end - start)

        return result
    return wrapper

def log_io(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Input: args=%s, kwargs=%s", args, kwargs)

        result = func(*args, **kwargs)

        logging.info("Output: %s", result)

        return result
    return wrapper

def admin_only(func):
    @wraps(func)
    def wrapper(role, *args, **kwargs):
        if role != "admin":
            logging.warning("Access denied for role: %s", role)
            return None

        logging.info("Access granted")
        return func(role, *args, **kwargs)
    return wrapper

@timing
@log_io
@admin_only
def delete_user(role, username):
    return f"User {username} deleted successfully"

delete_user("admin", "Ali")
delete_user("guest", "Sara")
