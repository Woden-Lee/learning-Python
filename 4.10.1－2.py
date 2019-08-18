s = input('请输入元素，以空格隔开\n')
spam = s.split(' ')
'''spam = []
print('Please input what you need')
r = input(' ')
print('Please input what you want')
for i in int (r) - 1:
	spam[i] = input(' ')'''
for a in range(len(spam)):
	if a == len(spam) - 1:
		print ('and ' + spam[a])
	else:
		print(spam[a], end= ',')