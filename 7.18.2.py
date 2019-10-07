import re

def strip(text,word):
	if len(word) == 0:
		word = r'\s'
	stword = r'^(%s)*|(%s)*$' %(word,word)
	regex1 = re.compile(stword)
	a = regex1.sub('',text)
	print(a)

print('Please input the text:')
t = input()
print('Please input the word:')
w = input()
strip(t,w)