import random

print("enter the number of clients in the star ")
client = int(input(""))
print("Enter the number of 'slots':")
no_slots = int(input(""))

client_list = []
for i in range(client):
	client_list.append(0)



fifo = {}
contention = {}

for i in range(no_slots):
	no_clients = random.randint(0, client)
	rand_list = []
	for j in range(no_clients):
		new_rand = random.randint(0, client)
		while(new_rand in rand_list):
			new_rand = random.randint(0, client)
		rand_list.append(new_rand)
	if(len(rand_list)>1):
		contention[i] = rand_list
	else:
		fifo[i] = rand_list

	print("fifo: ", fifo, "contention:", contention)


