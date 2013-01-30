class InfixOperator:
    def __init__(self, function):
        self.function = function
    def __rlshift__(self, other):
        return InfixOperator(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)
mult = InfixOperator(lambda x,y: x*y)
div = InfixOperator(lambda x,y: x/y)

print 2 <<mult>> 4
print 2 <<div>> 4
