#!/usr/bin/python3

import random
#This is the script for simulating the Goodbye ALOHA! protocol

def tree_split(arr,n):
	mini = -1
	tmp = -1

	for i in range(len(arr)):
		if len(arr[i])>1:
			if len(arr[i]) > mini:
				mini = len(arr[i])
				tmp = i
	queue = []
	for i in range(len(arr)):
		if len(arr[i])>1:
			queue.append(arr[i])

	for i in range(len(queue)):
		for j in range(i, len(queue)):
			if(len(queue[j])>len(queue[i])):
				queue[i], queue[j] = queue[j], queue[i]


	for j in range(len(queue)):
		new_arr = []
		for i in range(n):
			new_arr.append([])
		pos = 0
		for i in queue[j]:
			new_arr[pos].append(i)
			pos = (pos+1)%(n-1)
			
		tree_split(new_arr,n)

	if len(queue)==0:
		lol.append(arr)

print("enter the number of clients in the star ")
client = int(input(""))
print("Enter the number of time slots")
time_slots = int(input(""))
print("Enter the number of 'slots':")
no_slots = int(input(""))



no_packets = 0
packets_received = 0

client_list = []
for i in range(client):
	client_list.append(0)




for j in range(time_slots):
	print("time slot:", j+1)
	# for i in range(no_slots):
	# 	no_clients = random.randint(0, client)
	# 	rand_list = []
	# 	for j in range(no_clients):
	# 		new_rand = random.randint(0, client)
	# 		while(new_rand in rand_list):
	# 			new_rand = random.randint(0, client)
	# 		rand_list.append(new_rand)
	# 	if(len(rand_list)>1):
	# 		contention[i] = rand_list
	# 	else:
	# 		fifo[i] = rand_list
	fifo = {}
	contention = {}
	rand_list = {}
	for i in range(no_slots):
		rand_list[i] = []


	#Generate random contentions for the slots available
	for i in range(client):
		
		slot = random.randint(0,no_slots-1)
		no_packets+=1
		rand_list[slot].append(i)
	L = []
	#if there is a collision, add to CRQ. Else, add to DTQ.
	for i in rand_list:
		L.append(rand_list[i])
		if len(rand_list[i])>1:
			contention[i] = rand_list[i]
		else:
			fifo[i] = rand_list[i]
	lol =[]

	#Run the tree splitting algorithm on items in the CRQ
	tree_split(L , no_slots)
	



	print("fifo: ", fifo, "contention:", contention)
	print(lol)
	dropped = 0
	for i in lol:
		for j in i:
			if(len(j)>0):
				dropped = dropped +1
	packets_received -= len(lol)*dropped

print("Total number of packets sent:", no_packets)
print("Number of packets received:", packets_received+no_packets)
print("Throughput:", float(packets_received+no_packets)/no_packets)