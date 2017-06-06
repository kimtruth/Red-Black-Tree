class Node:
	RED = 'R'
	BLACK = 'B'
	
	def __init__(self, newval):
		self.val = newval
		self.p = None
		self.color = None
		self.left = NilNode()
		self.right = NilNode()	

	def __bool__(self):
		return True
		
class NilNode:
	def __init__(self):
		self.val = None
		self.p = None
		self.color = Node.BLACK
		self.left = None
		self.right = None

	def __bool__(self):
		return False