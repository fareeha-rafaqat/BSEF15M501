#!usr/bin/env python


time_on_gantt_chart=0
start_time_of_process=0
processes={}
burst_time=[]
n = input("Enter the number of processes:")
for i in range (0,n):
	arrival_time=input("Arrival Time:")
	b_time=input("Burst Time:")
	burst_time.append(b_time)
	processes[burst_time[i]] = [i+1 , arrival_time]

print "Arrival Time           Burst Time"
for i in range (0,n):
	print processes.get(burst_time[i])[1], "\t\t\t" , burst_time[i] 

burst_time.sort()
time_on_gantt_chart = processes.get(burst_time[0])[1]
start_time_of_proces=time_on_gantt_chart

for i in range (0,n):
	time_on_gantt_chart+= burst_time[i]
	print start_time_of_process , "________" , time_on_gantt_chart
	start_time_of_process = time_on_gantt_chart

