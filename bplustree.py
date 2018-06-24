from bisect import bisect_right


class Tree(object):
	factor = int()
	intfac = int()
	def __init__(self):
		self.root = None
		
	def getRoot(self):
		return self.root


	def insert(self, val):
		if not self.root:
			print("Root not defined. Making a root of the bplus Tree")
			self.root = Node(T,[val])

		else:
			self.root.insert(val)
			# print(self.root)

	def delete(self,val):
		self.root.delete(val)

		if not self.root.children:
			self.root = False

	def printTree(self):
		print(self.root)
		for child in self.root.children:
			print(child)

class Node(object):
	leaffactor = Tree.factor
	interiorfactor = Tree.intfac
	def __init__(self,T,keys,parent=None,isLeaf=True):
		self.isLeaf = isLeaf
		self.parent = parent
		self.keys = list() or keys
		self.children = list()
		self.next = None
		self.prev = None
		self.tree = T

	def insert(self,val):
		index = bisect_right(self.keys,val)
		
		if not self.isLeaf:
			# print("Going to the index",index)
			self.children[index].insert(val)
		else:
			if index < len(self.keys) and self.keys[index] == val:
				print("Not adding duplicate, improve this code"\
				 "to either add frequency or link to the other value as key value pair")
			else:
				self.keys.insert(index,val)
				# print("Now keys are",self.keys)
				self.balance()


	def balance(self):
		# print(self)
		if len(self.keys) > Tree.factor:
			half = (Tree.factor-1)//2		
			right = list()
			left = self.keys[:half+1]
			value_to_push = self.keys[half+1]
			# print(value_to_push)
			if self.isLeaf:
				right = self.keys[half+1:]
			else:
				right = self.keys[half+2:]
				

			if not self.parent:
				# print(left,right)
				self.tree.root = self.parent
				self.parent = Node(self.tree,[],None,False)
				
				self.keys = left
				self.parent.keys = [value_to_push]
				right = Node(self.tree,right,self.parent,self.isLeaf)

				if self.isLeaf:
					self.next = right
					right.prev = self

				self.parent.children = [self,right]
				self.tree.root = self.parent
			else:
				
				index = bisect_right(self.parent.keys, value_to_push)
				# print(left,right,value_to_push,index)
				self.keys = left
				right = Node(self.tree,right,self.parent,self.isLeaf)
				# print(self.keys,right.keys)
				if self.isLeaf:
					self.next = right
					right.prev = self

				self.parent.children.insert(index+1,right)
				self.parent.keys.insert(index,value_to_push)
				

			self.parent.balance()



	def delete(self,val):
		if self.isLeaf:
			try:
				self.keys.remove(val)
			except:
				raise ValueError("Could not find ",val)
			self.rearrage()
		else:
			index = bisect_right(self.keys,val)
			self.children[index].delete(val)


	def rearrage(self):
		if len(self.keys) < (Node.factor+1)//2:
			if self.isLeaf:
				sibling,index = None,None
				if self.next:
					sibling = self.next
					index = 0
				else:
					sibling = self.prev
					index = -1

				if len(self.sibling.keys) <= (Node.factor+1)//2:
					parent = self.parent
					if not parent:
						return
					self.next.left = self.left
					self.next.keys = self.keys+self.next.keys
					self.parent.children.pop(0)
					self.parent.keys.pop(bisect_right(self.parent.keys,self.keys[0]))
					self.parent.delete()
				else:
					index = bisect_right(self.parent.keys,self.keys[0])
					self.keys.append(self.sibling[index])
					self.sibling.pop(0)
					self.parent.keys[index] = self.sibling.keys[index]
			else:
				pass

	def __str__(self):
		string = "Keys are: "+str(self.keys)
		string += "\nchildren are: "+str([child.keys for child in self.children])
		string += "\nroot node is: "+str(self.tree.root.keys)
		if self.prev:
			string += "\nleft sibling is: "+str(self.prev.keys)
		if self.next:
			string += "\nright sibling is:"+str(self.next.keys)
		return string

Tree.factor = 3
Tree.intfact = 3
T = Tree()
for i in [1,4,16,25,9,20,13,15]:
	T.insert(i)
while True:
	x = int(input())
	if x == -1:
		break
	T.insert(x)
	# T.printTree()
