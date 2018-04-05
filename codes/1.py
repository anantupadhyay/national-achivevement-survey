l1 = ['a', 'b', 'c']
l2 = ['b', 'd']

l3 = []
for x in l1:
	if x in l2:
		l3.append(x)
print("Elements common to both list are")
print l3
'''
	alternatively
	print (list(set(l1).intersection(l2)))
'''
#------------------------------------------------------------------------------

l4 = []
for x in l1:
	if not x in l2:
		l4.append(x)
print("Elements in l1 that are not in l2")
print l4

'''
The following can also be used:
'''
print list(set(l1) - set(l2))