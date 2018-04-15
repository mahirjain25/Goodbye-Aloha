#!/usr/bin/python3

import random
import tree_split 

print("enter the number of clients in the star ")
client = int(input(""))
print("Enter the number of time slots")
time_slots = int(input(""))
print("Enter the number of 'slots':")
no_slots = int(input(""))

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

	for i in range(client):
		
		slot = random.randint(0,no_slots-1)
		rand_list[slot].append(i)
	L = []
	for i in rand_list:
		L.append(rand_list[i])
		if len(rand_list[i])>1:
			contention[i] = rand_list[i]
		else:
			fifo[i] = rand_list[i]
	tree_split.tree_split(L , no_slots)



	print("fifo: ", fifo, "contention:", contention)
