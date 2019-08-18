def code(spam):
	for a in range(len(spam)):
		if a == len(spam) - 1:
			print ('and ' + spam[a])
		else:
			print(spam[a], end= ',')
s = input('请输入元素，以空格隔开\n')
spam = s.split(' ')
code(spam)