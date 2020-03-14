def WhoisOlder(**ages):
    name = ''
    if len(ages) != 0:
        ans = max(ages.values())
    else:
        print('None is oldest.')
        return -1
    for key in ages.keys():
        if ages[key] == ans:
            name = key
            break
    print(f'{name} is the oldest.')
    return ans

#if __name__ == '__main__':
 #   print(WhoisOlder(Amy=10, Lisa=20))
