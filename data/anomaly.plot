set datafile separator ","
#set yrange[0:1200]

plot "anomaly_scores.csv" with line

pause -1
