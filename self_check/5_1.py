s1 = input('Enter a sentence: ')
s2 = input('Enter prohibited list: ')

L1 = list(s1)
L2 = list(s2)
ans = []
for item in L1:
    if item not in L2:
        ans.append(item)
print(ans)



