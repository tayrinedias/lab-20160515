import json 

f = open('50linhasfd.txt')
for l in f:
	# print(l, end='')
	print('A string tem',len(l),'caracteres.')
	if l:
		obj = obj = json.loads(l)
		print(obj['id'])