def printTable (talist):
	maxwide = [0] * len(talist)
	for roll1 in  range(len(talist)):
		max = 0
		for roll2 in range(len(talist[roll1])):
			if len(talist[roll1][roll2]) > max:
				max = len(talist[roll1][roll2])
			maxwide[roll1] = max
	for roll1 in range(len(talist)):
		for roll2 in range(len(talist[roll1])):
			print(talist[roll1][roll2].rjust(maxwide[roll1]))

tabledata = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]

printTable(tabledata)
			