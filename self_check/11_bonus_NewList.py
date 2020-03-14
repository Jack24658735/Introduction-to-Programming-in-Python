import itertools
class NewList(list):
    def __repr__(self):
        return self.__class__.__name__ +'('+ super().__repr__() + ')'
    def __matmul__(self, RHS):
        #ans = [(x, y) for x in self for y in RHS]
        #ans = NewList(ans)
        #return ans
        ans = list(itertools.product(self, RHS))
        ans = NewList(ans)
        return ans
    def __rmul__(self, scalar):
        ans = NewList()
        for item in self:
            item *= scalar
            ans.append(item)
        return ans
    def __getitem__(self, itemref):
        if type(itemref) == int:
            if itemref < 0:
                return super().__getitem__(itemref)
            elif itemref > 0:
                return super().__getitem__(itemref - 1)
            else:
                raise ValueError
        elif type(itemref) == slice:
            start, end, step = itemref.start, itemref.stop, itemref.step
            if step == None:
                itemref = slice(start - 1, end, step)
            elif step >= 0:
                itemref = slice(start - 1, end, step)
            elif step < 0:
                itemref = slice(start - 1, end - 2, step)
            return NewList(super().__getitem__(itemref))
    def __setitem__(self, itemref, val):
        if type(itemref) == int:
            if itemref < 0:
                return super().__setitem__(itemref, val)
            elif itemref > 0:
                return super().__setitem__(itemref - 1, val)
            else:
                raise ValueError
        elif type(itemref) == slice:
            start, end, step = itemref.start, itemref.stop, itemref.step
            if step == None:
                itemref = slice(start - 1, end, step)
            elif step >= 0:
                itemref = slice(start - 1, end , step)
            elif step < 0:
                itemref = slice(start - 1, end - 2, step)
            return super().__setitem__(itemref, val)
    def __delitem__(self, itemref):
        if type(itemref) == int:
            if itemref < 0:
                return super().__delitem__(itemref)
            elif itemref > 0:
                return super().__delitem__(itemref - 1)
            else:
                raise ValueError
        elif type(itemref) == slice:
            start, end, step = itemref.start, itemref.stop, itemref.step
            if step == None:
                itemref = slice(start - 1, end, step)
            elif step >= 0:
                itemref = slice(start - 1, end , step)
            elif step < 0:
                itemref = slice(start - 1, end - 2, step)
            return super().__delitem__(itemref)
