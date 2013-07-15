#!/usr/bin/env python
from pylab import *
import csv,sys,os,re

if len(sys.argv) < 2:
    sys.exit('Usage: %s directory' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
	sys.exit('ERROR: Directory %s was not found!' % sys.argv[1])
listOfCSVFiles=[]
configFile=[]
for r,d,files in os.walk(sys.argv[1]):
    for file in files:
        if file.endswith(".csv"):
        	listOfCSVFiles.append(os.path.join(r,file))
	elif file.endswith(".config"):
		configFile=os.path.join(r,file)	
if not configFile:
	sys.exit('ERROR: Config file was not found!')
listOfColumnElements=[]
with open(configFile,'rb') as file:
	reader=csv.reader(file)
	for row in reader:
		for element in row:
			listOfColumnElements.append(element)

isAValidDigit=re.compile('\d+(\.\d+)?')
listOfRows=[]
for filename in listOfCSVFiles:
	with open(filename,'rb') as file:
		reader=csv.reader(file)
		for row in reader:
			listOfRows.append(row)

listOfColumns=zip(*listOfRows)
print "Possible Elements:"
for i in listOfColumnElements:
	print i

while True:
	input=raw_input('XAxis YAxis : ').split()
	if "exit" in input:
		break
	try:
		x = np.array([t for t in listOfColumns[listOfColumnElements.index(input[0])] if not isAValidDigit.match(t) == None],np.float64)
		y = np.array([t for t in listOfColumns[listOfColumnElements.index(input[1])] if not isAValidDigit.match(t) == None],np.float64)
		scatter(x,y, marker='+', c='r')
		xlabel(input[0])
		ylabel(input[1])
		fit =polyfit(x,y,1)
		fit_fn=poly1d(fit)
		plot(x,fit_fn(x),'--k')
		show()
	except Exception: 
	  pass



