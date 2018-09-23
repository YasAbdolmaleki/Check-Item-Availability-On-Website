from crontab import CronTab

cron = CronTab(user='yasabdolmaleki')

def scheduleScript():	  
	job = cron.new(command='python /Users/yasabdolmaleki/Documents/Shopping Script/CheckItemAvailability.py')  
	job.minute.every(1)
	cron.write()
	print "Job is valid: " + str(job.is_valid())

def removeJobs():
	#for job in cron:
	#	cron.remove(job)
	cron.remove_all() 
	print "Job removed"

def printAllJobs():
	for job in cron:
		print job

#scheduleScript()
removeJobs()
printAllJobs()
