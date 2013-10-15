class Stack:
	# The internal representation of a stack. We'll be using a list.
	data = list()
	# This keeps track of the current top location in the stack.
	idx = 0
	def __init__(self):  
		#  Don't worry about this method--I'll talk about this when we talk
		#  some more about classes.
		print("Stack created")

	def push(self,item):
		if len(self.data) > self.idx: #This is how items should be added to the stack
			self.data[self.idx] = item
			self.idx += 1
		else: #This must exist to extend the size of the list when it fills up
			self.data.append(item)
			self.idx += 1

	def pop(self):
		if self.idx == 0: # You can't pop if the stack is empty.
			return None
		# Otherwise, return the item at the top of the stack.
		self.idx -= 1
		return self.data[self.idx]
