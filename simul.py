import random

#Creating the possible array of vertices. All vertices have a value from 1 to m*n.
def grid(m,n):
    value_list = []
    j = 1
    for item in range(n):
        row_list = []
        for item in range(m):
            row_list.append(j)
            j = j + 1
        value_list.append(row_list)
    return value_list
    #print(value_list)

#Finding the neighbor list of all vertices. The output is a list of dictionaries with index, value, and neighbor list.
#Neighbors are horizontally and vertically adjacent vertices.
#credits to GitHub: MaxRudometkin
def find_neighbours(arr):

    neighbors = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):

            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])  # top neighbor
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1])  # right neighbor
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j])  # bottom neighbor
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])  # left neighbor

            else:
                # add neighbors
                new_neighbors = [
                    arr[i - 1][j],  # top neighbor
                    arr[i][j + 1],  # right neighbor
                    arr[i + 1][j],  # bottom neighbor
                    arr[i][j - 1]   # left neighbor
                ]

            neighbors.append({
                "index": i * len(arr[i]) + j,
                "value": value,
                "neighbors": new_neighbors})

    #print(neighbors)
    return neighbors


arr = grid(5,4)
list_of_dict = find_neighbours(arr)
list_of_dict_for_removal = list_of_dict

#print(list_of_dict)
#print(list_of_dict_for_removal)

#all_nodes = [i["value"] for i in list_of_dict]
#print(all_nodes)

#selecting one of the values to start the game
random_index = random.randint(0,len(list_of_dict)-1)
first_node_dict = list_of_dict[random_index]
first_node = first_node_dict["value"]
#print("Printing first node *********")
#print(first_node)
path_list = []
path_list.append(first_node)

first_node_neighbor_list = (first_node_dict["neighbors"])

random_index_again = random.randint(0,len(first_node_neighbor_list)-1)
selected_node = first_node_neighbor_list[random_index_again]
#print("Printing second node *********")
#print(selected_node)
path_list.append(selected_node)
#print("Printing the starting edge *********")
#print(path_list)

def removal(node):

    #remove the first two nodes from all neighbor lists
    for i in list_of_dict:
        try:
            i["neighbors"].remove(node)
        except ValueError:
            #print("could not find {} in {}".format(j,i["neighbors"]))
            continue

removal(first_node)
removal(selected_node)

#print(list_of_dict)

while True:

    #randomly choosing one of the vertex from the existing path
    next_node = random.choice([path_list[0], path_list[len(path_list)-1]])
    #print("Printing next node ********* ")
    #print(next_node)

    #removing the selected node from all neighbor lists
    removal(next_node)

    if next_node == path_list[0]:

        next_node_dict = list_of_dict[next_node-1]
        next_neighbors = next_node_dict["neighbors"]
        #print("Printing next node neighbors *******")
        #print(next_neighbors)
        if len(next_neighbors) == 0:
            break

        next_next_neighbor = random.choice(next_neighbors)
        #print("Printing chosen neighbor *******")
        #print(next_next_neighbor)

        #removing the selected node from all neighbor lists
        removal(next_next_neighbor)

        path_list.insert(0, next_next_neighbor)

    elif next_node == path_list[len(path_list)-1]:

        next_node_dict = list_of_dict[next_node-1]
        next_neighbors = next_node_dict["neighbors"]
        #print("Printing next node neighbors *******")
        #print(next_neighbors)
        if len(next_neighbors) == 0:
            break

        next_next_neighbor = random.choice(next_neighbors)
        #print("Printing chosen neighbor *******")
        #print(next_next_neighbor)

        #removing the selected node from all neighbor lists
        removal(next_next_neighbor)

        path_list.append(next_next_neighbor)

print(path_list)

path_length = len(path_list)

if path_length%2 == 0:
    print("Player 1 won.")
else:
    print("Player 2 won.")
