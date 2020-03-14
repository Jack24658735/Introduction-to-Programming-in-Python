import sys

tiki_colors = ['red', 'yellow', 'blue', 'green', 'purple', 'pink', 'orange', 'brown', 'grey']

while True:
    inst = input("What's your operation? ")
    if inst == 'help':
        with open('Operation_list.txt', 'r') as fh:
            for line in fh.readlines():
                print(line, end = '')
            print()
    elif inst == 'look':
        with open('Tiki_line.txt', 'r') as fh:
            for line in fh.readlines():
                print(line, end = '')
            print()
    elif inst == 'Tiki up 1':
        L = []
        with open('Tiki_line.txt', 'r') as fh:
            L = fh.readlines()
        ans = ''.join(L)
        ans = ans.split()
        color = input('Select your target color: ')
        if color not in tiki_colors:
            sys.stderr.write('Error: Invalid target\n')
        else:  
            for i in range(len(ans)):
                if ans[i] == color:
                    if i - 2 < 1:
                        sys.stderr.write("Error: You can't do this operation.\n")
                        break
                    ans[i], ans[i - 2] = ans[i - 2], ans[i]
                    break
        final = ''
        for j in range(len(ans)):
            if j % 2 == 1:
                final += ans[j] + '\n'
            else:
                final += ans[j] + ' '               
        with open('Tiki_line.txt', 'w') as fh:
            fh.write(final)

    elif inst == 'Tiki up 2':
        L = []
        with open('Tiki_line.txt', 'r') as fh:
            L = fh.readlines()
        ans = ''.join(L)
        ans = ans.split()
        color = input('Select your target color: ')
        if color not in tiki_colors:
            sys.stderr.write('Error: Invalid target\n')
        else:
            for i in range(len(ans)):
                if ans[i] == color:
                    if i - 4 < 1:
                        sys.stderr.write("Error: You can't do this operation.\n")
                        break
                    ans[i], ans[i - 4] = ans[i - 4], ans[i]
                    ans[i], ans[i - 2] = ans[i - 2], ans[i]
                    break
        final = ''
        for j in range(len(ans)):
            if j % 2 == 1:
                final += ans[j] + '\n'
            else:
                final += ans[j] + ' '
        with open('Tiki_line.txt', 'w') as fh:
            fh.write(final)
    
    elif inst == 'Tiki up 3':
        L = []
        with open('Tiki_line.txt', 'r') as fh:
            L = fh.readlines()
        ans = ''.join(L)
        ans = ans.split()
        color = input('Select your target color: ')
        if color not in tiki_colors:
            sys.stderr.write('Error: Invalid target\n')  
        else:
            for i in range(len(ans)):
                if ans[i] == color:
                    if i - 6 < 1:
                        sys.stderr.write("Error: You can't do this operation.\n")
                        break
                    ans[i], ans[i - 6] = ans[i - 6], ans[i]
                    ans[i], ans[i - 4] = ans[i - 4], ans[i]
                    ans[i], ans[i - 2] = ans[i - 2], ans[i]
                    break
        final = ''
        for j in range(len(ans)):
            if j % 2 == 1:
                final += ans[j] + '\n'
            else:
                final += ans[j] + ' '
        with open('Tiki_line.txt', 'w') as fh:
            fh.write(final)
    elif inst == 'Reset':
        reset = "#1 red\n#2 yellow\n#3 blue\n#4 green\n#5 purple\n#6 pink\n#7 orange\n#8 brown\n#9 grey\n"
        with open('Tiki_line.txt', 'w') as fh:
            fh.write(reset)
    elif inst == 'Tiki Topple':
        L = []
        with open('Tiki_line.txt', 'r') as fh:
            L = fh.readlines()
        ans = ''.join(L)
        ans = ans.split()
        color = input('Select your target color: ')
        if color not in tiki_colors:
            sys.stderr.write('Error: Invalid target\n')
        else:
            for i in range(len(ans)):
                if ans[i] == color:
                    while i + 2 <= len(ans):
                        ans[i], ans[i + 2] = ans[i + 2], ans[i]
                        i += 2
                    break
        final = ''
        for j in range(len(ans)):
            if j % 2 == 1:
                final += ans[j] + '\n'
            else:
                final += ans[j] + ' '
        with open('Tiki_line.txt', 'w') as fh:
            fh.write(final)

    elif inst == 'Tiki Toast':
        L = []
        with open('Tiki_line.txt', 'r') as fh:
            L = fh.readlines()
        if len(L) <= 3:
            sys.stderr.write("Error: You can't do this operation.\n")
        else:
            L.pop()
            with open('Tiki_line.txt', 'w') as fh:
                fh.writelines(L)
    elif inst == 'quit':
        print('Goodbye!')
        break
    else:
        sys.stderr.write('Error: Invalid operation.\n')
        
    
