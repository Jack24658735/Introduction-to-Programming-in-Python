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
'''
# For judging purpose
instantiate_generator1 = input()
exec(instantiate_generator1)
instantiate_generator2 = input()
exec(instantiate_generator2)
for i in range(4):
    test_code = input()
    exec(test_code)
'''
