class CountingList(list):
    def __init__(self, d = []):
        super().__init__(d)
        access_count = []
        for idx in d:
            access_count.append(0)
        self._access_count = access_count
    def __getitem__(self, i):
        if type(i) == int:
            self._access_count[i] += 1
        else:   #i is slice
            start, stop, step = i.start, i.stop, i.step
            while start < stop:
                self._access_count[start] += 1
                if step != None:
                    start += step
                else:
                    start += 1
        return super().__getitem__(i)
    def __iter__(self):
        tmp = []
        ans = []
        for i in range(len(self)):
            tmp.append((self._access_count[i], self[i]))
        tmp.sort(reverse = True)
        ans = [item[1] for item in tmp]
        #for item in tmp:
            #ans.append(item[1])
        return iter(ans)

        
