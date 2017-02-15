from csv import reader
from matplotlib import pyplot

with open('disease_person3_converted_out.csv','r') as f:
	data=list(reader(f))
 
print data[0]

temp=[i[3] for i in data[1:]]

print temp


pyplot.plot(range(len(temp)), temp)
pyplot.show()
