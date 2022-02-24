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
	first_node = (node_list[random_index])
	#print(first_node)

	#creating the neighbor list of the selected coordinate
	x = first_node[0]
	y = first_node[1]
	#print(x,y)

	neighbor_list =[[x,y],[x-1,y],[x,y-1], [x+1,y], [x,y+1]]
	#print(neighbor_list)	
	
	#need to code for nuances in neighbors. corners have only two neighbors. sides have only two.
	#as the game progresses, neighbors can only be from the list not already in selected	
	
	
main_list(5,3)


