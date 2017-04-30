#!usr/bin/env python


time_on_gantt_chart= 0
priority=[]
processes={}
n = input("Enter the number of processes:")
for i in range (0,n):
	prio_no=input("Priority number:")
	priority.append(prio_no)
	arrival_time=input("Arrival Time:")
	burst_time=input("Burst Time:")
	processes[priority[i]] = [i+1 , arrival_time , burst_time]

print "Priority#	Arrival Time           Burst Time"
for i in range (0,n):
	print priority[i] , "\t\t\t" ,  processes.get(priority[i])[1], "\t\t\t" ,  processes.get(priority[i])[2]

priority.sort()

print "Priority#	Arrival Time           Burst Time"
for i in range (0,n):
	print priority[i] , "\t\t\t" ,  processes.get(priority[i])[1], "\t\t\t" ,  processes.get(priority[i])[2]

time_on_gantt_chart = processes.get(priority[0])[1]
start_time_of_process=time_on_gantt_chart
for i in range (0,n):
	time_on_gantt_chart += processes.get(priority[i])[2]
	print start_time_of_process , "________" , time_on_gantt_chart
	start_time_of_process = time_on_gantt_chart
