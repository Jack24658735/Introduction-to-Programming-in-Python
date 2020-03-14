def CharRange(start, end):
    #ans = ''
    if ord(end) >= ord(start):
        for i in range(ord(end) - ord(start) + 1):
            yield chr(ord(start) + i)
            #ans += chr(ord(start) + i)
        #return ans
    else:
        for i in range(ord(start) - ord(end) + 1):
            yield chr(ord(start) - i)
            #ans += chr(ord(start) - i)
        #return ans
