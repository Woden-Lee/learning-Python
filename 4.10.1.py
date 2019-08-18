spam = ['apples' , 'bananas', 'tofu', 'cats']
for a in range(len(spam)):
	if a == len(spam) - 1:
		print ('and ' + spam[a])
	else:
		print(spam[a], end= ',')