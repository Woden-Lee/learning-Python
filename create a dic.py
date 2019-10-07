import pprint
dict = {}
while True:
      print('Please input the key and finish with nothing')
      k = input()
      if k == '':
      	break
      if k in dict:
      	print('Please input the value')
      	i = input()
      	dict[k] += int(i)
      else:
      	print('Please input the value')
      	i = input()
      	v = 0
      	v += int(i)
      	dict[k] = v

pprint.pprint(dict)