L = []
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
		L.append(arr)




a =[[1,2,3,4],[5],[6,7]]
tree_split(a,3)
print(L)
