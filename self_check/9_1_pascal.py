def pascal(row, column):
    if column == 0 or column == row:
        return 1
    else:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)

def print_Pascal_triangle(n):
    #L = list(range(n))
    #L = list(map(lambda x: str(x), L))
    #s1 = ' '.join(L)
    #print(f'Col: {s1}')
    
    # n rows
    for row in range(n): 
        #print(f'Row {row}: ', end = '')
        ans = ''
        for col in range(row + 1):
            ans += str(pascal(row, col)) + ' '
        print(ans)
    #L = list(range(n))
    #s1 = ' '.join(L)
    #print(f'Col: {s1}')

    #pascal(n, 0)
if __name__ == '__main__':
    print_Pascal_triangle(10)
