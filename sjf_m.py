#!usr/bin/env python

time_on_gantt_chart = 0
processes={}
burst_time=[]

def take_input():
	n = input("Enter the number of processes:")	
	for i in range (0,n):
		arrival_time=input("Arrival Time:")
		b_time=input("Burst Time:")
		burst_time.append(b_time)
		processes[burst_time[i]] = [i+1 , arrival_time]
	return n

def give_output(n):
	print "Arrival Time           Burst Time"
	for i in range (0,n):
		print processes.get(burst_time[i])[1], "\t\t\t" , burst_time[i] 

def sorting():
	burst_time.sort()
def sjf(n):
	time_on_gantt_chart = processes.get(burst_time[0])[1] #arrival time of shortest process
	start_time_of_process = time_on_gantt_chart
	for i in range (0,n):
		time_on_gantt_chart += burst_time[i]
		print start_time_of_process , "________" , time_on_gantt_chart
		start_time_of_process = time_on_gantt_chart
no_of_processes = take_input()
give_output(no_of_processes)
sorting()
sjf(no_of_processes)

