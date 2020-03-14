import random
random.seed(0) # You must initiate the random seed to 0 for judging purpose.

class Matrix:
    def __init__(self, data):
        self._rows = []
        for item in data:
            self._rows.append(item)
        self._cols = list(map(list, list(zip(*data))))
        #zip will construct tuple, but we may need list

    def row(self, r):
        return self._rows[r]

    def column(self, c):
        return self._cols[c]

    @property
    def nrows(self):
        return len(self._rows)
    @property
    def ncolumns(self):
        return len(self._cols)
    def transpose(self):
        M_trans = self._cols
        return Matrix(M_trans)
    def randomize(self):
        flatten = []
        for item in self._rows:
            flatten.extend(item)    
        random.shuffle(flatten)
        ans = [flatten[i:i + self.ncolumns] for i in range(0, len(flatten), self.ncolumns)]
        return Matrix(ans)
        #ans = []
        #start = 0
        #tmp_end = self.n + 1 #plus one for inclusive
        #while tmp_end < self.nrows * self.ncolumns:
        #    tmp = flatten[start:tmp_end]
        #    start += tmp_end
        #    tmp_end *= 2
        #    ans.append(tmp)
 
    def __matmul__(self, other):     
        tmp = []
        if self.ncolumns == other.nrows:
            for i in range(self.nrows):
                for j in range(other.ncolumns):
                    L1 = list(zip(self.row(i), other.column(j)))
                    ans = sum(list(map(lambda x: x[0] * x[1], L1)))
                    tmp.append(ans)
        ans = [tmp[i:i + other.ncolumns] for i in range(0, len(tmp), other.ncolumns)]
        return Matrix(ans)
