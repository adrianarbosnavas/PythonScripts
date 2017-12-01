#!/usr/bin/python
import os

rootdir = ''

replacements = {'src':'target'}

logData = []

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		lines = []
		fullPath = os.path.join(subdir, file)
		logData.append("Looking in file: %s\n" % file)
		with open(fullPath) as infile:
			for line in infile:
				linebc = line
				for src, target in replacements.items():
					line = line.replace(src,target)
					if(linebc!=line):
						logData.append(linebc+' -> '+line+'\n')
				lines.append(line)
		with open(fullPath, 'w') as outfile:
			for line in lines:
				outfile.write(line)
with open(rootdir+'/log', 'w') as logfile:
			for line in logData:
				logfile.write(line)
