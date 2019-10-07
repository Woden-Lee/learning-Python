def displayInventory(dict):
	print('Inventory:')
	i = 0
	for k,v in dict.items():
		print(str(v) +'  '+ k)
		i += v
	print('total number is :' + str(i))

#将新列表添加至新字典
def addToInventory(ndict,nlist):
	for r in range(len(nlist)):
		if nlist[r] in ndict:
			ndict[nlist[r]] += 1
		else:
			ndict[nlist[r]] = 1
	return(ndict)

#比较新旧字典并更新数据
def compare(odict,ndict):
	for nkey in ndict:
		if nkey in odict:
			ovalue = odict[nkey]
			ndict[nkey] += int(ovalue)
		else:
			return
	return(ndict)

inventory = {'arrow':12,'gold coin':42,'rope':1,'torch':6,'dagger':1}
new = {}
dragonLoot = ['gold coin','dagger','gold coin','ruby']

addToInventory(new,dragonLoot)
compare(inventory,new)
displayInventory(new)