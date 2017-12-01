#!/usr/bin/python
import os

# Directory to loop
rootdir = 'directory'

# List of extensions to delete
extToDelete = ['.ext']

logData = []

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		fullPath = os.path.join(subdir, file)
		for ext in extToDelete:
			if fullPath.endswith(ext):
				logData.append('Removing -> ' + fullPath + '\n')
				os.remove(fullPath)
				
for subdir, dirs, files in os.walk(rootdir):
	for directories in dirs:
		fullPath = os.path.join(subdir, directories)
		if not os.listdir(fullPath):
			os.rmdir(fullPath)
			
with open(rootdir+'/log', 'w') as logfile:
			for line in logData:
				logfile.write(line)
