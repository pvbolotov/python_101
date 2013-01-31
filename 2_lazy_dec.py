from functools import wraps

def lazyness_maker(decorator):
    @wraps(decorator)
    def lazy_decorator(function):
        @wraps(function)
        def decorated_func(*args, **kwargs):
            return decorator(function)(*args, **kwargs)
        return decorated_func
    return lazy_decorator

@lazyness_maker
def dummy_decorator(func):
    print "dummy_decorator is now calling " + func.__name__
    return func

@dummy_decorator
def dummy_function():
    print "I am dummy_function"

print "Before calling dummy function"
dummy_function()
