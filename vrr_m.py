#!usr/bin/env python

total = 0
processes={}
arrival_time=[]
burst_time=[]

def take_input():
	n = input("Enter the number of processes:")
	for i in range (0,n):
		a_time=input("Arrival Time:")
		arrival_time.append(a_time)
		b_time=input("Burst Time:")
		burst_time.append(b_time)
		processes[arrival_time[i]] = [i+1 , burst_time[i]]
	return n
def input_slice_time():
	time_slice = input("Enter the time slice:")
	return time_slice
def input_io():
	io = input("Enter the input ouput waiting time:")
	return io
def output(n):
	print "Arrival Time           Burst Time"
	for i in range (0,n):
		print arrival_time[i], "\t\t\t" , burst_time[i]
def sorting():
	arrival_time.sort()

def vrr(n, time_slice,io):
	count_the_terminated_processes  = 0
	total = 0 #gantt chart's total time
	while (count_the_terminated_processes != n):
		for i in range (0,n):
			check = 0 #check that after subtracting if the burst time has become negative then don't let it enter
			check = processes.get(arrival_time[i])[1] #burst_time of the process
			if(check!=-1):
				check = check - time_slice
				if(check > 0):
					total+=(processes.get(arrival_time[i])[1] - check)
					processes[arrival_time[i]] = [i+1 , check]	
				elif(check<=0):
					count_the_terminated_processes+=1
					check*=(-1)
					total+=check
					processes[arrival_time[i]] = [i+1 , -1]
				print(total)

no_of_processes=take_input()
time=input_slice_time()
io=input_io()
output(no_of_processes)
sorting()
vrr(no_of_processes,time,io)
