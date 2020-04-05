s1 = input('Enter a string:\n')
s2 = input('Enter another string:\n')
if len(s2) < len(s1):
	print('Shorter string: %s (length %d)' % (s2, len(s2)))
	print('Longer string: %s (length %d)' % (s1, len(s1)))
if len(s1) < len(s2):
	print('Shorter string: %s (length %d)' % (s1, len(s1)))
	print('Longer string: %s (length %d)' % (s2, len(s2)))
if len(s1) == len(s2):
	print('First string: %s (length %d)' % (s1, len(s1)))
	print('Second string: %s (length %d)' % (s2, len(s2)))
