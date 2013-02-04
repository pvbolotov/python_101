# -*- coding: utf8 -*-

class Xrange(object):

    #конструктор
    def __init__(self, *args):
        if(len(args) == 0):
            raise TypeError("Xrange requires 1-3 int arguments")
        elif(len(args)>3):
            raise TypeError("Xrange can take no more than 3 int values as parameters")
        else:
            for i in args:
                if(i is None):
                    raise TypeError("An integer is required as a param")
        self._slice = slice(*args)
        if(self._slice.start >= self._slice.stop and (self._slice.step is None or self._slice.step >0)):
            self._slice = slice(0,0,1)
        if(self._slice.start<=self._slice.stop and self._slice.step is not None and self._slice.step <0):
            self._slice = slice(0,0,1)
        if self._slice.stop < 0 and self._slice.start is None and self._slice.step is None:
            self._slice = slice(0, self._slice.stop, -1)

    #"слайсовые" свойства - start, stop, step
    @property
    def start(self):
        if self._slice.start is None:
            return 0
        return self._slice.start
    @property
    def stop(self):
        return self._slice.stop
    @property
    def step(self):
        if self._slice.step is None:
            return 1
        elif self._slice.step == 0:
            raise TypeError("Slice step cannot be zero")
        return self._slice.step

    #comparing two objects
    def __cmp__(self, other):
        return (cmp(type(self), type(other)) or cmp(self._slice, other._slice))

    #implementing calling len() function
    def __len__(self):
        if abs(self.stop - self.start) % self.step == 0:
            return abs((self.stop - self.start)/(self.step))
        else:
            return abs((self.stop - self.start)/(self.step))+1

    def _index(self, i):
        return self.start + self.step*i

    #__getitem__ - это то же самое, что обращение к элементу с помощью []
    def __getitem__(self, index):
        #если получаем на вход не один индекс (то есть объект нужно "слайснуть")
        if isinstance(index, slice):
            start, stop, step = index.indices(self.__len__())
            return Xrange(self._index(start), self._index(stop), step*self.step)
        #если получаем на вход один индекс
        elif isinstance(index, (int,long)):
            if index >= 0:
                i=index
            else:
                i = index + self.__len__()
            if (i<0) or (i>= self.__len__()):
                raise IndexError("Index out of bounds")
            return self._index(i)
        else:
            raise TypeError("only slice or plain idex notations are maintained")

#tests section

assert list(Xrange(1,10)) == list(xrange(1,10))
assert list(Xrange(3,-20)) == list(xrange(3,-20))
assert list(Xrange(-3,3)) == list(xrange(-3,3))
assert list(Xrange(-10,-20)) == list(xrange(-10,-20))

assert list(Xrange(1,2,3)) == list(xrange(1,2,3))
assert list(Xrange(5,7,-9)) == list(xrange(5,7,-9))
assert list(Xrange(12,-7,9)) == list(xrange(12,-7,9))
assert list(Xrange(-22,7,2)) == list(xrange(-22,7,2))
assert list(Xrange(-19,-7,2)) == list(xrange(-19,-7,2))
assert list(Xrange(22,-7,-2)) == list(xrange(22,-7,-2))
assert list(Xrange(-22,7,-3)) == list(xrange(-22,7,-3))
assert list(Xrange(-13,-4,-1)) == list(xrange(-23,-4,-1))

assert 1 in Xrange(23)
assert 22 in Xrange(23)
assert 23 not in Xrange(23)

assert Xrange(3, 25, 2)[4:][1] == 13
assert Xrange(1, 10, 2)[:4][3] == 7
assert Xrange(7, 20, 2)[::-1][0] == 19
assert Xrange(5, 10, 3)[::-1][-1] == 5
assert Xrange(8, 36, 2)[7:4:-1][0] == 22
assert Xrange(3, 33, 3)[2:0:-1][-1] == 6
