def displayInventory(dict):
	print('Inventory:')
	i = 0
	for k,v in dict.items():
		print(str(v) +'  '+ k)
		i += v
	print('total number is :' + str(i))

inventory = {'arrow':12,'gold coin':42,'rope':1,'torch':6,'dagger':1}

displayInventory(inventory)