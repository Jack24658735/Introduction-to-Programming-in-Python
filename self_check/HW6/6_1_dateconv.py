def leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0)


if __name__ == "__main__":
    Months = ['January', 'February', 'March', 'April', 'May',
              'June', 'July', 'Augest', 'September', 'October', 'November', 'December']
    while True:
        str = input('Enter data in mm/dd/yyyy: ')
        if str == 'quit':
            print('bye')
            break
        else:
            L = str.split('/')
            month = int(L[0])
            day = int(L[1])
            year = int(L[2])
            is_leap = leap_year(year)

            if month < 1 or month > 12:
                print(f'Invalid month {month}: should be between 01 and 12')
            # by conditional expressions
            if month in {1, 3, 5, 7, 8, 10, 12}:
                print(f'{Months[month - 1]} {day}, {year}' if (day >= 1 and day <= 31)
                      else f'Invalid day for {Months[month - 1]}: should be between 01..31')
            elif month in {4, 6, 9, 11}:
                print(f'{Months[month - 1]} {day}, {year}' if day >= 1 and day <= 30
                      else f'Invalid day for {Months[month - 1]}: should be between 01..30')
            elif month == 2:
                if day == 29 and is_leap == True:
                    print(f'{Months[month - 1]} {day}, {year}')
                elif day == 29 and is_leap == False:
                    print(f'Invalidate day 29 for Feburary: not a leap year')
                elif day >= 1 and day <= 28:
                    print(f'{Months[month - 1]} {day}, {year}')
                else:
                    print(
                        f'Invalid day for {Months[month - 1]}: should be between 01..28')
