#Не поддерживает *args, **kwargs и дефолтные значения

def currying_dec(fun, *args, **kwargs):
    if(len(args) + len(kwargs)) >= fun.__code__.co_argcount:
        return fun(*args, **kwargs)
    return (lambda *add_args, **add_kwargs: currying_dec(fun, *(args + add_args), **dict(kwargs, **add_kwargs)))

@currying_dec
def multiply(a,b,c,d):
    return a*b*c*d

assert multiply(1,2,3,5) == 30
assert multiply(1,2,3)(5) == 30
assert multiply(1,2)(3,5) == 30
assert multiply(1)(2,3,5) == 30
assert multiply(1)(2,3)(5) == 30

