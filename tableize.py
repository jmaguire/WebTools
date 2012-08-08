import csv

#Pivots a table

#f is the name of the data file
#Column0 becomes row name
#Column1 becomes a column name
#Column2 holds the value for the corresponding row/column name

#labels is a row vector of column names. 
#note you generally must add the name for column0 to labels.csv
f = 'Departments'

dataReader = csv.reader(open(f+'.csv'))
labelsReader = csv.reader(open('labels.csv'))
dataWriter = csv.writer(open('pretty'+f+'.csv','wb'))

toWrite = []
for line in labelsReader:
	toWrite.append(line[0])
dataWriter.writerow(toWrite)
toWrite = []
for line in dataReader:
	if not toWrite:
		toWrite.append(line[0])
	if toWrite[0] != line[0]:
		dataWriter.writerow(toWrite)
		toWrite = [line[0]]
	toWrite.append(line[-1])
dataWriter.writerow(toWrite)
print 'done'