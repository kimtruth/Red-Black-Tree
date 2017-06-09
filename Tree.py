from Node import Node, NilNode

class RBT:
	def __init__(self):
		self.root = None

	def left_rotate(self, x):
		y = x.right
		x.right = y.left
		if y.left:
			y.left.p = x
		y.p = x.p
		if not x.p:
			self.root = y
		elif x == x.p.left:
			x.p.left = y
		else:
			x.p.right = y
		y.left = x
		x.p = y

	def right_rotate(self, y):
		x = y.left
		y.left = x.right
		if x.right:
			x.right.p = y
		x.p = y.p
		if not y.p:
			self.root = x
		elif y == y.p.left:
			y.p.left = x
		else:
			y.p.right = x
		x.right = y
		y.p = x

	def insert_fixup(self, z):
		while z.p.color == Node.RED:
			if z.p == z.p.p.left:
				y = z.p.p.right
				if y and y.color == Node.RED:
					z.p.color = Node.BLACK
					y.color = Node.BLACK
					z.p.p.color = Node.RED
					z = z.p.p
				else:
					if z == z.p.right:
						z = z.p
						self.left_rotate(z)
					z.p.color = Node.BLACK
					z.p.p.color = Node.RED
					self.right_rotate(z.p.p)
			else:
				y = z.p.p.left
				if y and y.color == Node.RED:
					z.p.color = Node.BLACK
					y.color = Node.BLACK
					z.p.p.color = Node.RED
					z = z.p.p
				else:
					if z == z.p.left:
						z = z.p
						self.right_rotate(z)
					z.p.color = Node.BLACK
					z.p.p.color = Node.RED
					self.left_rotate(z.p.p)
		self.root.color = Node.BLACK

	def insert(self, z):
		z = Node(z)
		y = NilNode()
		x = self.root
		while x:
			y = x
			if z.val < x.val:
				x = x.left
			else:
				x = x.right
		z.p = y
		if not y:
			self.root = z
		elif z.val < y.val:
			y.left = z
		else:
			y.right = z
		z.color = Node.RED
		self.insert_fixup(z)

	def print(self, tree, level):
		if tree.right:
			self.print(tree.right, level + 1)
		for i in range(level):
			print('   ', end='')
		print(tree.color, tree.val)
		if tree.left:
			self.print(tree.left, level + 1)

	def node_count(self, tree = None):
		if tree == None: tree = self.root

		if not tree:
			return 0
		return self.node_count(tree.left) + self.node_count(tree.right) + 1

	def black_node_count(self, tree = None):
		if tree == None: tree = self.root

		if not tree:
			return 0
		elif tree.color == Node.BLACK:
			return self.black_node_count(tree.left) + self.black_node_count(tree.right) + 1
		else:
			return self.black_node_count(tree.left) + self.black_node_count(tree.right)

	def black_height(self):
		x = self.root
		height = 0
		while x:
			x = x.left
			if x.color == Node.BLACK:
				height += 1
		return height

	def transplant(self, u, v):
		if not u.p:
			self.root = v
		elif u == u.p.left:
			u.p.left = v
		else:
			u.p.right = v
		v.p = u.p

	def minimum(self, tree):
		while tree.left:
			tree = tree.left
		return tree

	def delete_fixup(self, x):
		while x != self.root and x.color == Node.BLACK:
			if x == x.p.left:
				w = x.p.right
				if w.color == Node.RED:
					w.color = Node.BLACK
					x.p.color = Node.RED
					self.left_rotate(x.p)
					w = x.p.right
				if w.left.color == Node.BLACK and w.right.color == Node.BLACK:
					w.color = Node.RED
					x = x.p
				else:
					if w.right.color == Node.BLACK:
						w.left.color = Node.BLACK
						w.color = Node.RED
						self.right_rotate(w)
						w = x.p.right
					w.color = x.p.color
					x.p.color = Node.BLACK
					w.right.color = Node.BLACK
					self.left_rotate(x.p)
					x = self.root
			else:
				w = x.p.left
				if w.color == Node.RED:
					w.color = Node.BLACK
					x.p.color = Node.RED
					self.right_rotate(x.p)
					w = x.p.left
				if w.right.color == Node.BLACK and w.left.color == Node.BLACK:
					w.color = Node.RED
					x = x.p
				else:
					if w.left.color == Node.BLACK:
						w.right.color = Node.BLACK
						w.color = Node.RED
						self.left_rotate(w)
						w = x.p.left
					w.color = x.p.color
					x.p.color = Node.BLACK
					w.left.color = Node.BLACK
					self.right_rotate(x.p)
					x = self.root
		x.color = Node.BLACK


	def delete(self, z):
		if not z:
			return -1
		y = z
		y_origin_color = y.color
		if not z.left:
			x = z.right
			self.transplant(z, z.right)
		elif not z.right:
			x = z.left
			self.transplant(z, z.left)
		else:
			y = self.minimum(z.right)
			y_origin_color = y.color
			x = y.right

			if y.p == z:
				x.p = y
			else:
				self.transplant(y, y.right)
				y.right = z.right
				y.right.p = y
			self.transplant(z, y)
			y.left = z.left
			y.left.p = y
			y.color = z.color
		if y_origin_color == Node.BLACK:
			self.delete_fixup(x)
		
	def search(self, val, tree = None):
		if tree == None: tree = self.root

		if not tree:
			#print('[*] search error : %d is not in tree' % (val))
			return tree
		if tree.val == val:
			return tree
		elif val < tree.val:
			return self.search(val, tree.left)
		else:
			return self.search(val, tree.right)

	def inorder(self, tree):
		if not tree:
			return
		else:
			self.inorder(tree.left)
			self.inorder(tree.right)
			print(tree.val,tree.color)