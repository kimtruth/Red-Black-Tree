import os
from Tree import RBT


rbt = RBT()
txt = open('input.txt').read()
datas = list(map(int, txt.split('\n')[:-1]))

txt = open('search.txt').read()
searchs = list(map(int, txt.split('\n')[:-1]))

insert = 0
delete = 0
miss = 0
for data in datas:
	if data > 0:
		rbt.insert(data)
		insert += 1
	elif data < 0:
		n = rbt.search(-data)
		if rbt.delete(n) == -1:
			miss += 1
		else:
			delete += 1
	else:
		break

a = rbt.inorderTraversal(rbt.root)
a = ['NIL', 'NIL'] + a + ['NIL', 'NIL']

f = open('output.txt', 'w')
for d in searchs:
	for i in range(2, len(a) - 2):
		if d == a[i]:
			f.write(' '.join(map(str, a[i-1:i+2])) + '\n')
			break
		elif d < a[i]:
			f.write('{0} NIL {1}\n'.format(a[i-1], a[i]))
			break
	else:
		f.write('{0} NIL NIL\n'.format(a[i]))
f.close()
