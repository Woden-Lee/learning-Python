def displayInventory(dict):
	print('Inventory:')
	i = 0
	for k,v in dict.items():
		print(str(v) +'  '+ k)
		i += v
	print('total number is :' + str(i))

#固定字典计数
#inventory = {'arrow':12,'gold coin':42,'rope':1,'torch':6,'dagger':1}

#自定义字典输入并计数
inventory = {}
while True:
      print('Please input the key and finish with nothing')
      k = input()
      if k == '':
      	break
      if k in inventory:
      	print('Please input the value')
      	i = input()
      	inventory[k] += int(i)
      else:
      	print('Please input the value')
      	i = input()
      	v = 0
      	v += int(i)
      	inventory[k] = v

displayInventory(inventory)