from Tree import RBT

rbt = RBT()

filename = input('filename= ')
txt = open(filename).read()
datas = list(map(int, txt.split('\n')))

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

print('total =', rbt.node_count())
print('insert =', insert)
print('deleted =', delete)
print('miss = ', miss)
print('nb =', rbt.black_node_count())
print('bh =', rbt.black_height())

rbt.inorder(rbt.root)
