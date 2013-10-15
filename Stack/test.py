from stack import Stack


#  This creates a new instance of the Stack, named s
#  All stack operations can be performed on s, such as popping and pushing
#  by specifying s.push(item) and s.pop()
s = Stack()

#  A simple program I created to show how this program is used.
#  "push [item]" will push something onto the stack
#  "pop" will pop the top item off the stack
#  "print" will show what is inside the data of the stack at a given time
#  Try printing after you pop something off the stack to see what happens!
while True:
	line = input()
	if line == "exit":
		break
	line = line.split(" ")
	if line[0] == "push":
		print("--> Pushing %s" % line[1])
		s.push(line[1])
	elif line[0] == "pop":
		print("--> Popped %s" % s.pop())
	elif line[0] == "print":
		print("--> data: %s" % s.data)
		print("--> index: %i" % s.idx)
	else:
		print("Command not recognized")
