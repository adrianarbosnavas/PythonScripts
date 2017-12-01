#!/usr/bin/python
import os
import shutil

# Directory to loop
rootdir = 'directory'
ordereddir = 'orderedImg'
ordereddirpath = os.path.join(rootdir, ordereddir)

# List of extensions
extToCheck = ['.jpg', '.jpeg', '.png', '.gif']

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		fullPath = os.path.join(subdir, file)
		for ext in extToCheck:
			if fullPath.endswith(ext):
				tempfilename = file.split("-")
				date = tempfilename[1]
				dateDir = os.path.join(ordereddirpath, date)
				if not os.path.exists(dateDir):
					os.makedirs(dateDir)
				shutil.move(fullPath,dateDir)
