
'''
This program works by representing the Printer and each Job as an object. The Printer class contains two important functions: addJob and printJob. When reading in the data initially, you use addJob to put the new job into the printer queue. When printing jobs out later, you use printJob to print the next job in the queue, according to the rules specified in the question.

The functions __init__() and __str__() are special python functions. If you don't know what they do, ask me next club meeting.
'''

class Printer:
	def __init__(self):
		self.data = list()
	def addJob(self,job):
		self.data.append(job)
	def searchForHigherPriority(self,priority):
		'''
		Returns:
			True if a job higher than priority exists in the queue
			False otherwise
		'''
		for job in self.data:
			if job.priority > priority:
				return True
		return False
	def printJob(self):
		job = self.data.pop(0)
		while self.searchForHigherPriority(job.priority):
			self.data.append(job)
			job = self.data.pop(0)
		return job
	def __str__(self):
		ret = "["
		for job in self.data:
			ret += "%s, "%str(job)
		return ret[:-1] + "]"

class Job:
	priority = 0
	mine = False
	def __str__(self):
		return "Job(%s,%s)" % (self.priority, self.mine)





'''
Down here is where the real program starts.
'''
numTestCases = input() #The first number is the number of test cases
for i in range(int(numTestCases)):
	# make a new printer for each test case...
	p = Printer()

	# read in all the data about this test case
	line = input().split(" ")
	numJobs = int(line[0])
	myJob = int(line[1])
	line = input().split(" ")

	# put all the jobs in the queue
	for j in range(numJobs):
		job = Job()
		job.priority = line[j]
		if j == myJob:
			job.mine = True
		p.addJob(job)
	
	# print jobs until you find yours, and keep track of the time
	time = 1
	while not p.printJob().mine:
		time += 1
	
	# print out the result to the screen
	print(time)
