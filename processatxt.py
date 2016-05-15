import json 

f = open('50linhasfd.txt')
for l in f:
	# print(l, end='')
	print('A string tem',len(l),'caracteres.')
	if l.strip():
		obj = obj = json.loads(l)
		print(obj['id'])
		print(obj['created_at'])
		print(obj['text'])
		print(obj['user'['screen_name']])
