import datetime
import tkinter


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

if __name__ == '__main__':
    root = tkinter.Tk()
    f = tkinter.Frame(root, borderwidth = 5)
    f.grid(row = 0, column = 0)
        
    result = tkinter.Listbox(f)
    result.grid(row = 1, column = 2, rowspan = 6, columnspan = 2)
    
    tmp_ans = []

    operand_str = tkinter.StringVar()
    operand_entry = tkinter.Entry(f, textvariable = operand_str)
    operand_entry.grid(row = 6, column = 0)

    def enter(value):
        global tmp_ans
        global operand_entry
        tmp_ans.append(value)
        operand_entry.insert(tkinter.END, value + ' ')
    def final_date():
        global result
        global operand_entry
        tmp = operand_entry.get()
        tmp = str(tmp)
        tmp = ''.join(tmp)
        print(tmp)

        final = datecalc(tmp)
        #operand_entry.delete(0, tkinter.END)
        for i, w in enumerate(final):
            result.insert(i, w)
    
    today_bt = tkinter.Button(f, text = 'today', command = lambda: enter('today'))
    today_bt.grid(row = 0, column = 0, sticky = 'W')

    tomorrow_bt = tkinter.Button(f, text = 'tomorrow', command = lambda: enter('tomorrow'))
    tomorrow_bt.grid(row = 1, column = 0, sticky = 'W')

    yesterday_bt = tkinter.Button(f, text = 'yesterday', command = lambda: enter('yesterday'))
    yesterday_bt.grid(row = 2, column = 0, sticky = 'W')

    add_bt = tkinter.Button(f, text = 'add', command = lambda: enter('add'))
    add_bt.grid(row = 3, column = 0, sticky = 'W')

    sub_bt = tkinter.Button(f, text = 'sub', command = lambda: enter('sub'))
    sub_bt.grid(row = 4, column = 0, sticky = 'W')

    swap_bt = tkinter.Button(f, text = 'swap', command = lambda: enter('swap'))
    swap_bt.grid(row = 5, column = 0, sticky = 'W')

    push_bt = tkinter.Button(f, text = 'push', command = lambda: final_date())
    push_bt.grid(row = 6, column = 1)
    
    error_label = tkinter.Label(f, text = 'error message here')
    error_label.grid(row = 7, column = 0, columnspan = 1)
    
    clear_bt = tkinter.Button(f, text = 'clear', command = lambda: result.delete(0, tkinter.END))
    clear_bt.grid(row = 7, column = 2, sticky = 'W')
    
    quit_bt = tkinter.Button(f, text = 'quit', command = root.destroy)
    quit_bt.grid(row = 7, column = 3, sticky = 'E')
    

    
    tkinter.mainloop()
