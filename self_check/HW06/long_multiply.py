def long_multiply(a, b):
    str_a = str(a)
    str_b = str(b)
    L_a = len(str_a)
    L_b = len(str_b)
    L_product = len(str(a * b))
    width = max(L_a, L_b + 2, L_product)
    
    ans = [str_a.rjust(width), 'x)' + str_b.rjust(width - 2), '-' * width]
    for i in range(L_b):
        ans.append(str((int(str_b[L_b - i - 1]) * a)))
        ans[i + 3] = ans[i + 3].rjust(width - i)
    ans.extend(['-' * width, str(a * b).rjust(width)]) 
    
    return '\n'.join(ans)


if __name__ == "__main__":
    print(long_multiply(65768, 6666432))
