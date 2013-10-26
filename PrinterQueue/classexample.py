
class PrintJob:
	priority = 0
	isMine = False





somejob = PrintJob()
somejob.priority = 2
somejob.isMine = True


otherjob = PrintJob()
otherjob.priority = 3


print(somejob.isMine)
print(otherjob.priority)


info = list()
queue = list()

for i in range(1,4):
	info.append(i)

for i in range(1,4):
	job = PrintJob()
	job.priority = i
	if i == 2:
		job.isMine = True
	queue.append(job)


print(info)
for i in queue:
	print("%s %s" %(i.priority,i.isMine))
