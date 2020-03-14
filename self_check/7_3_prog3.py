import sys
try:
    fh = open(sys.argv[1], 'w')
    while True:
        #fh = open(sys.argv[1], 'w')
        s = input('Enter your text or Enter "quit" to finish program:' ) + '\n'
        if s == 'quit\n':
            break        
        fh.write(s)
    fh.close()
except FileNotFoundError:
    print('There is an exception. It is FileNotFoundError.')

