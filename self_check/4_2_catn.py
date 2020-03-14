import sys
numberOfArgs = len(sys.argv)
if numberOfArgs < 2:
    sys.stderr.write('Usage: %s inputFile\n' % sys.argv[0])
    sys.exit(1)

linenumber = 1
if sys.argv[1] == '-n':
    for filename in sys.argv[2:]:
        try:
            fh = open(filename, 'r')
        except:
            sys.stderr.write('cannot open input file %s\n' % filename)
            sys.exit(2)
        for line in fh.readlines():
            print('   %3d  ' % linenumber, end = '')
            print(line, end = '')
            linenumber += 1
        fh.close()
        linenumber = 1
else:
    for filename in sys.argv[1:]:
        try:
            fh = open(filename, 'r')
        except:
            sys.stderr.write('cannot open input file %s\n' % filename)
            sys.exit(2)
        for line in fh.readlines():
            print(line, end = '')
        fh.close()

