def adjacency_list_to_matrix(adjacency_list:dict):
    # find the number of nodes in the graph
    num_nodes = len(adjacency_list)

    # create a num_nodes x num_nodes matrix filled with 0s
    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    # go through each node and its list of connected nodes
    for node, neighbors in adjacency_list.items():
        # go through each neighbor connected to the current node
        for neighbor in neighbors:
            # mark an edge to neighbor with a 1
            matrix[node][neighbor] = 1

    # print each row of the matrix
    for row in matrix:
        print(row)

    # return the completed matrix
    return matrix