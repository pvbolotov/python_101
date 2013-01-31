# -*- coding: utf-8 -*-
import itertools

def Ireduce(func, iterable, initial_val=None):
    if initial_val is None:
        iterable = iter(iterable)
        current_val = iterable.next()
    else:
        current_val = initial_val
    for x in iterable:
        current_val = func(current_val, x)
        yield current_val

assert list(Ireduce(lambda x,y: x+y, (1,2,3,4,5))) == [3,6,10,15]
assert list(Ireduce(lambda x,y: x+y, (1,2,3,4,5), -1)) == [0,2,5,9,14]
assert list(Ireduce(lambda x,y: x+y, (1,2,3,4,5), 1)) == [2,4,7,11,16]
