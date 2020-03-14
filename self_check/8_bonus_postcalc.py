def postcalc(*operand, stack = []):
    L = []
    ans = []
    for item in operand:
        L.append(item)
    L = stack + L
    for obj in L:
        if obj == 'add':
            tmp1 = ans.pop()
            tmp2 = ans.pop()
            ans.append(tmp1 + tmp2)
        elif obj == 'sub':
            tmp1 = ans.pop()
            tmp2 = ans.pop()
            ans.append(tmp1 - tmp2)
        elif obj == 'mul':
            tmp1 = ans.pop()
            tmp2 = ans.pop()
            ans.append(tmp1 * tmp2)
        elif obj == 'swap':
            tmp1 = ans.pop()
            tmp2 = ans.pop()
            ans.append(tmp1)
            ans.append(tmp2)
        else:
            ans.append(obj) 
    return ans
