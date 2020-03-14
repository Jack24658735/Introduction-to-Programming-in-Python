import sys

try:
    with open(sys.argv[1], 'r') as fh:
        for line in fh.readlines():
            print(line, end = '')  

except FileNotFoundError:
    print('There is an exception. It is FileNotFoundError.')
