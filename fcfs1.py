#!usr/bin/env python


time_on_gantt_chart = 0
processes={}
n = input("Enter the number of processes:")
for i in range (0,n):
	
	arrival_time=input("Arrival Time:")
	burst_time=input("Burst Time:")
	processes[i+1] = [arrival_time , burst_time]

print "Arrival Time           Burst Time"
for i in range (1,n+1):
	print processes.get(i)[0], "\t\t\t" , processes.get(i)[1] 

time_on_gantt_chart= processes.get(1)[0]
start_time_of_process=time_on_gantt_chart

for i in range (1,n+1):
	time_on_gantt_chart= time_on_gantt_chart + processes.get(i)[1]
	print start_time_of_process , "________" ,time_on_gantt_chart
	start_time_of_process= time_on_gantt_chart

