def printTable (talist):
	maxwide = [0] * len(talist)
	a = len(talist)
	for roll1 in  range(len(talist)):
		b = len(talist[roll1])
		max = 0
		for roll2 in range(len(talist[roll1])):
			if len(talist[roll1][roll2]) > max:
				max = len(talist[roll1][roll2])
			maxwide[roll1] = max
	for q in range(b):
		for p in range(a):
			print(talist[p][q].rjust(maxwide[p]),end = ' ')
		print(' ')

tabledata = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]

printTable(tabledata)
			