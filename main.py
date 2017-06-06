from Tree import RBT

rbt = RBT()

txt = open('input.txt').read()
datas = list(map(int, txt.split('\n')))

for data in datas:
	if data > 0:
		rbt.insert(data)
	elif data < 0:
		n = rbt.search(-data)
		rbt.delete(n)
	else:
		break

print('total =', rbt.node_count())
print('nb =', rbt.black_node_count())
print('bh =', rbt.black_height())
rbt.inorder(rbt.root)
