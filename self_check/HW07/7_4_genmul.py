L = [i * j for i in range(1, 6) for j in range(1, 8)]
count = 0
for item in L:
    count += 1
    print(f'{item} ', end = '')
    if count == 7:
        print()
        count = 0
