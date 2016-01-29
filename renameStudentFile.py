import gettext
import re
import os
import subprocess
from optparse import OptionParser

parser = OptionParser(description='Utility will attempt to grab the student name from a pdf and rename the file using his/her name. If the directory is not specified it looks in the current directory for two folders named tobeconverted and converted. The folders should be created beforehand and one of them should contain the PDFs.',version="%prog 1.0")
parser.add_option('-f', dest='fromd', help='source directory', default=os.getcwd()+"\\tobeconverted", metavar="PATH")
parser.add_option('-t', dest='tod', help='destination directory', default=os.getcwd()+"\\converted", metavar="PATH")

(opts, args) = parser.parse_args()

if not os.path.exists(opts.fromd):
	print "\nThe folder you have entered does not exist. Please try again. If you have spaces in the folder path you should use double quotes!\n"
	parser.print_help()
	exit(-1)
else:
	convfile = opts.fromd
if not os.path.exists(opts.tod):
	print "\nThe folder you have entered does not exist. Please try again. If you have spaces in the folder path you should use double quotes!\n"
	parser.print_help()
	exit(-1)
else:
	tofile = opts.tod

print "From directory: " + convfile
print "To directory: " + tofile

file = ""

files = os.listdir(convfile)

if len(files) <= 1:
	print "\nNothing to convert! Good bye :)\n"
	exit(0)
	
print files
for mfile in files:
	if '.pdf' in mfile:
		file = convfile + "\\" + mfile
		mtext = gettext.main(file)
		myF = open ('file', 'r')

		#print myF.readline()
	
		m = re.search('name:(.+?)(form|tutor|class)', myF.readline(), re.IGNORECASE)
		if m:
			found = m.group(1)
			#print found.strip() + " - " + mfile
		myF.close
		mtext = 0
		
		m = re.search('(.+?)[A-Z`]{2,}',found)
		if m:
			firstName = m.group(1)
			#print firstName + " - " + found
		
		
		m = found.partition(firstName)
		surname = m[2]
			
		command = "copy \"" + convfile + "\\" + mfile + "\" \"" + tofile + "\\" + surname + " " + firstName + ".pdf\""
		subprocess.call(command, shell=True)
exit(0)
