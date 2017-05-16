#!usr/bin/env python

time_on_gantt_chart = 0
processes={}
arrival_time=[]

def take_input():
	n = input("Enter the number of processes:")	
	for i in range (0,n):
		a_time=input("Arrival Time:")
		arrival_time.append(a_time)
		b_time=input("Burst Time:")
		processes[arrival_time[i]] = [i+1 , b_time]
	return n

def give_output(n):
	print "Arrival Time           Burst Time"
	for i in range (0,n):
		print arrival_time[i], "\t\t\t" , processes.get(arrival_time[i])[1]

def sorting():
	arrival_time.sort()
def fcfs(n):
	time_on_gantt_chart = arrival_time[0] #arrival time of shortest process
	start_time_of_process = time_on_gantt_chart
	for i in range (0,n):
		time_on_gantt_chart += processes.get(arrival_time[i])[1] #get burst_time
		print start_time_of_process , "________" , time_on_gantt_chart
		start_time_of_process = time_on_gantt_chart
no_of_processes = take_input()
give_output(no_of_processes)
sorting()
fcfs(no_of_processes)

