import os.path
import sys

#get path to files
fromFileFull = raw_input("Enter the full list folder: ")
if(os.path.isfile(fromFileFull)):
    print 'Ok'
else:
	sys.exit("No such file")

fromFileShort = raw_input("Enter the comparison folder: ")
if(os.path.isfile(fromFileShort)):
    print 'Ok'
else:
	sys.exit("No such file")

ulist = open(fromFileFull, 'r')
clist = open(fromFileShort, 'r')
res = open('result.txt', 'w')

fullList = []
countList = []
toDelete = []

for line in ulist:
	line = line.rstrip('\n')
	fullList.append(line)

ulist.close()

for line in clist:
	line = line.rstrip('\n')
	countList.append(line)

clist.close()
	
toDelete = list(set(fullList) - set(countList))
toDelete.sort()

for elem in toDelete:
	res.write(elem)
	res.write('\n')

