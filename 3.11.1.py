def collatz():
	number = int(input(''))
	while number > 1:
		if number % 2 ==0:
			print(number // 2)
			number = number // 2
		else:
			print(3 * number + 1)
			number = 3 * number + 1
print('please enter number')
collatz()