import datetime
class date(datetime.date):
    #constructor is inherited
    def __repr__(self):
        return __class__.__name__ + f'({self.year}, {self.month}, {self.day})'

class days(datetime.timedelta):
    def __new__(cls, day, *args, **kwargs):
        return super().__new__(cls, day, *args, **kwargs)
    def __init__(self, day):
        self._days = day
    def __repr__(self):
        return __class__.__name__ + f'({self._days})'

class weeks(datetime.timedelta):
    def __new__(cls, week, *args, **kwargs):
        day = week * 7
        return super().__new__(cls, day, *args, **kwargs)
    def __init__(self, week):
        self._week = week
    def __repr__(self):
        return __class__.__name__ + f'({self._week})'
class months:
    def __init__(self, month):
        self._month = month
    def __repr__(self):
        return __class__.__name__ + f'({self._month})'       
    def __add__(self, RHS):
        if isinstance(RHS, date):
            day = RHS.day
            year = RHS.year
            month = RHS.month + self._month
            while month > 12: #keep doing until month lies in the range
                month -= 12
                year += 1
            return date(year, month, day)
        else:
            return months(RHS._month + self._month)
    def __sub__(self, RHS):
        if isinstance(RHS, date):
            day = RHS.day
            year = RHS.year
            month = RHS.month - self._month
            while month <= 0: #keep doing until month lies in the range
                month += 12
                year -= 1
            return date(year, month, day)
        else:
            return months(self._month - RHS._month)
            #change the direction?
    def __radd__(self, LHS):
        return self + LHS
    def __rsub__(self, LHS):
        day = LHS.day
        year = LHS.year
        month = LHS.month - self._month
        while month <= 0: #keep doing until month lies in the range
            month += 12
            year -= 1
        return date(year, month, day)


def datecalc(*operand):
    ans = []
    for obj in operand:
        if obj == 'add':
            tmp1 = ans.pop()
            tmp2 = ans.pop()
            tmp = tmp1 + tmp2
            #match the date format rather than datetime.date
            if isinstance(tmp1 + tmp2, datetime.date):
                tmp = date(tmp.year, tmp.month, tmp.day)
            ans.append(tmp)
        elif obj == 'sub':
            tmp1 = ans.pop()
            tmp2 = ans.pop()
            ans.append(tmp1 - tmp2)
        elif obj == 'swap':
            tmp1 = ans.pop()
            tmp2 = ans.pop()
            ans.append(tmp1)
            ans.append(tmp2)
        elif obj == 'today':
            tmp = date.today()
            tmp = date(tmp.year, tmp.month, tmp.day)
            ans.append(tmp)
        elif obj == 'tomorrow':
            tmp = date.today() + datetime.timedelta(days = 1)
            tmp = date(tmp.year, tmp.month, tmp.day)
            ans.append(tmp)
        elif obj == 'yesterday':
            tmp = date.today() - datetime.timedelta(days = 1)
            tmp = date(tmp.year, tmp.month, tmp.day)
            ans.append(tmp)
        else:  
            ans.append(obj) 
    return ans
