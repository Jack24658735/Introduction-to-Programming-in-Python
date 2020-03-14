import operator as op
class Polynomial:
    def __init__(self, *coeff):
        self._coeff = coeff
    def evaluate(self, xvalue):
        ans = 0
        for power, v in enumerate(self._coeff):
            ans += v * (xvalue ** power)
        return ans
    def __repr__(self):
        return self.__class__.__name__ + f"({', '.join(map(str, self._coeff))})"
    def __add__(self, right):
        L1 = len(self._coeff)
        L2 = len(right._coeff)
        tmp_coeff_1 = self._coeff
        tmp_coeff_2 = right._coeff
        if L1 < L2:
            for i in range(L2 - L1):
                tmp_coeff_1 += (0,)
        else:
            for i in range(L1 - L2):
                tmp_coeff_2 += (0,)
        return Polynomial(*map(op.add, tmp_coeff_1, tmp_coeff_2))
    def __sub__(self, right):
        L1 = len(self._coeff)
        L2 = len(right._coeff)
        tmp_coeff_1 = self._coeff
        tmp_coeff_2 = right._coeff
        if L1 < L2:
            for i in range(L2 - L1):
                tmp_coeff_1 += (0,)
        else:
            for i in range(L1 - L2):
                tmp_coeff_2 += (0,)
        return Polynomial(*map(op.sub, tmp_coeff_1, tmp_coeff_2))
    def __imul__(self, scale):
        #scaling = ()
        #for item in range(len(self._coeff)):
        #    scaling += (scale, )
        #self = Polynomial(*map(op.mul, self._coeff, scaling))
        self = Polynomial(*map(lambda x: 2 * x, self._coeff))
        return self
    __call__ = evaluate

if __name__ == '__main__':
    f = Polynomial(3, 2, 0, 5, 4)
    g = Polynomial(7, 4, 1)
    print(f + g)
    print(g - f)
    f *= 2
    print(f(1))
