# Python code to
# demonstrate readlines()



# writing to file
file1 = open('newdata', 'a')


# Using readlines()
file2 = open("/home/harash/Documents/MY_projects_withpython/learnings/data", 'r')
Lines = file2.readlines()

count = 0
# Strips the newline character
for line in Lines:
	count += 1
	if count%7==1:
		file1.write(line.strip()+"\n"+"\n")
file1.close()
