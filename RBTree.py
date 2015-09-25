from random import shuffle

class RedBlackTree:
	def __init__(self):
		self.root = None

	def __LeftRotate(self, node):
		y = node.right
		node.right = y.left
		if y.left:
			y.left.parent = node
		y.parent = node.parent
		if not node.parent:
			self.root = y
		elif node == node.parent.left:
			node.parent.left = y
		elif node == node.parent.right:
			node.parent.right = y
		y.left = node
		node.parent = y

	def __RightRotate(self, node):
		x = node.left
		node.left = x.right
		if x.right:
			x.right.parent = node
		x.parent = node.parent
		if not node.parent:
			self.root = x
		elif node == node.parent.left:
			node.parent.left = x
		elif node == node.parent.right:
			node.parent.right = x
		x.right = node
		node.parent = x

	def __RBTransplant(self, u, v):
		if not u.parent:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		if v:
			v.parent = u.parent


	def Insert(self, key):
		y = None
		x = self.root
		z = RedBlackNode(key)
		while x:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if not y:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
		self.__RBInsertFixup(z)
		return z

	def __RBInsertFixup(self, z):
		while z.parent and z.parent.red:
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y and y.red:
					z.parent.red = False
					y.red = False
					z.parent.parent.red = True
					z = z.parent.parent
				else:
					if z == z.parent.right:
						z = z.parent
						self.__LeftRotate(z)
					z.parent.red = False
					z.parent.parent.red = True
					self.__RightRotate(z.parent.parent)
			else:
				y = z.parent.parent.left
				if y and y.red:
					z.parent.red = False
					y.red = False
					z.parent.parent.red = True
					z = z.parent.parent
				else:
					if z == z.parent.left:
						z = z.parent
						self.__RightRotate(z)
					z.parent.red = False
					z.parent.parent.red = True
					self.__LeftRotate(z.parent.parent)
		self.root.red = False

	def Delete(self, z):
		y = z
		yOldRed = y.red
		if not z.left:
			x = z.right
			self.__RBTransplant(z, z.right)
		elif not z.right:
			x = z.left
			self.__RBTransplant(z, z.left)
		else:
			y = self.Minimum(z.right)
			yOldRed = y.red
			#NOT YET DONE

	def Minimum(self, start = self.root):
		if not start:
			return None
		while node.left:
			node = node.left
		return node



	def __str__(self):
		bunch = []
		self.__PrintEdges(0, 0, self.root, bunch)
		return 'graph RBTree{\n' + '\n'.join(bunch) + '\n}'

	def __PrintEdges(self, id, parent, node, bunch):
		if not node:
			return id
		id = id + 1
		if node.red:
			bunch.append('node_' + str(id) + '[label="'+ str(node.key) + '" fillcolor="#FFAAAA" style="filled"];')
		else:
			bunch.append('node_' + str(id) + '[label="'+ str(node.key) + '" fillcolor="#AAAAAA" style="filled"];')
		if node.parent and not node.parent.right:
			bunch.append('node_' + str(parent) + ':sw -- node_' +str(id)+';')
		elif node.parent and  not node.parent.left:
			bunch.append('node_' + str(parent) + ':se -- node_' +str(id)+';')
		elif node.parent:
			bunch.append('node_' + str(parent) + ' -- node_' +str(id)+';')
		next = id
		if node.left:
			next = self.__PrintEdges(id, id, node.left, bunch)
		if node.right:
			next = self.__PrintEdges(next, id, node.right, bunch)
		return next



class RedBlackNode:
	def __init__(self, key):
			self.left, self.right, self.parent, self.key, self.red = None, None, None, key, True


dataz = list(range(55))
shuffle(dataz)

t = RedBlackTree()

for i in dataz:
	t.Insert(i)

print(t)


