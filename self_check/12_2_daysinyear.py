D_month = {1: '01', 2: '02', 3:'03', 4: '04', 5: '05', 6: '06', \
         7: '07', 8: '08', 9: '09', 10:'10', 11: '11', 12: '12'}

D_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, \
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
class DaysInYear:
    def __init__(self, year):
        self._year = year
    def __getitem__(self, i):
        #leap(self._year)
        month = ''
        final_day = ''
        month_idx = 1
        if i >= 365:
            raise StopIteration
        else:
            if i < 31:
                month = D_month[1]
                final_day = i + 1
            else:
                for item in D_days.values():
                    if i >= 31:
                        i -= item
                        month_idx += 1
                    else:
                        break
                month = D_month[month_idx]
                final_day = i + 1
        ans = f'{self._year}.{month}.{final_day:02d}'
        return ans
    @staticmethod
    def leap(year):
        return (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0)  
