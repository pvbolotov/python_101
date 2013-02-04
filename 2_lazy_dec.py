from functools import wraps

def lazyness_maker(decorator):
    """
    This decorator allows another decorators to be invoked
    right in time when decorated function is called.
    Doesn't accept parametrized decorators
    """
    @wraps(decorator)
    def lazy_decorator(function):
        @wraps(function)
        def decorated_func(*args, **kwargs):
            return decorator(function)(*args, **kwargs)
        return decorated_func
    return lazy_decorator

def lazyness_maker_parametrized(decorator):
    """
    This decorator allows another decorators to be invoked
    right in time when decorated function is called.
    Accepts only parametrized decorators
    """
    @wraps(decorator)
    def lazy_decorator_with_params(*dec_args, **dec_kwargs):
        @wraps(decorator)
        def lazy_decorator(function):
            @wraps(function)
            def decorated_func(*f_args, **f_kwargs):
                return decorator(*dec_args, **dec_kwargs)(function)(*f_args, **f_kwargs)
            return decorated_func
        return lazy_decorator
    return lazy_decorator_with_params

#test section for lazyness_maker

d_call_counter=0

@lazyness_maker
def decorator_decrease_by_one(func):
    global d_call_counter
    d_call_counter += 1
    def decorated_func(x):
        return func(x) - 1
    return decorated_func

@decorator_decrease_by_one
def increase_by_two(x):
    return x+2

assert d_call_counter == 0
assert increase_by_two(10) == 11
assert d_call_counter == 1

#test section for lazyness_maker_parametrized

pd_call_counter = 0

@lazyness_maker_parametrized
def decorator_decrease_by_n(n):
    global pd_call_counter
    pd_call_counter += 1
    def inner_dec(func):
        def decorated_func(x):
            return func(x) - n
        return decorated_func
    return inner_dec

@decorator_decrease_by_n(5)
def increase_by_three(x):
    return x+3

assert pd_call_counter == 0
assert increase_by_three(2) == 0
assert pd_call_counter == 1
