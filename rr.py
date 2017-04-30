#!usr/bin/env python

start_time_of_process=0
processes={}
arrival_time=[]
burst_time=[]
n = input("Enter the number of processes:")
time_slice=input(" Enter the quantum time : ")
for i in range (0,n):
	arr_time=input("Arrival Time:")
	arrival_time.append(arr_time)
	b_time=input("Burst Time:")
	burst_time.append(b_time)
	processes[arrival_time[i]] = [i+1 , burst_time[i]]

print "Arrival Time           Burst Time"
for i in range (0,n):
	print arrival_time[i], "\t\t\t" ,  processes.get(arrival_time[i])[1]

arrival_time.sort()
count_the_terminated_process=0
total = 0
while(count_the_terminated_process!=n):

	for i in range (0,n):
		check=0
		check=processes.get(arrival_time[i])[1]
		if(check!=-1):
			check=check-time_slice
		if(check>0):
			burst_time[i]=check
			processes[arrival_time[i]] = [i+1 , burst_time[i]]
			total+=check
		if(check<=0):
			count_the_terminated_process+=1
			total+=burst_time[i]
			burst_time[i]=-1
			processes[arrival_time[i]] = [i+1 , burst_time[i]]
		print total
