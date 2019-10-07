import re

def test(password):
	if len(password) < 8:
		print('Your password should dayu 8 bits')
	else:
		regex1 = re.compile(r'[A-Z]')
		if regex1.search(password) == None:
			print('Your password should have the max word')
		else:
			regex2 = re.compile(r'[a-z]')
			if regex2.search(password) == None:
				print('Your password should have the min word')
			else:
				regex3 = re.compile(r'(\d)+')
				if regex3.search(password) == None:
					print('Your password should have the number')
				else:
					print('your password is safe')

print ('Please input your password:')
p = input()
test(p)
