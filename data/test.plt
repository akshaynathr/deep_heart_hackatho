set datafile separator ","

#Iplot \
#"healthy_person1_converted.csv" using 3 with lines, \
#"healthy_person2_converted.csv" using 3 with lines, \
#"healthy_person3_converted.csv" using 3 with lines, \
#"healthy_person4_converted.csv" using 3 with lines
#plot "disease_person1_converted.csv" using 3 with lines, \
#"disease_person2_converted.csv" using 3 with lines, \

plot "disease_person1.csv" using 3 with lines

pause -1
