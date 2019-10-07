def f(a,b,c):
	print('pi'.center(b+c,'*'))
	for k,v in a.items():
		print(k.ljust(b,'-') + str(v).rjust(c))
d = {'sandwish':4,'cookies':8000}
f(d,12,4)