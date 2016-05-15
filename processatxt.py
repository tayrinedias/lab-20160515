import json 

f = open('50linhasfd.txt')
for l in f:
	# print(l, end='')
	obj = obj = json.loads(l)
	print(obj['id'])