import random

#creating all possible list of coordinates (vertices)

def main_list(m,n):
	node_list = []
	i = 1
	for item in range(m):
		j = 1
		for item in range (n):
			nodes = [i,j]
			node_list.append(nodes)
			j = j + 1
		i = i + 1
	#print(node_list)

	#created node_list : a list of all possible coordinates

	#selecting one of the coordinates to start the game

	random_index = random.randint(0,len(node_list)-1)
	#print(node_list[random_index])

	#creating the neighbor list of the selected coordinate

	

	
	
	
main_list(5,3)