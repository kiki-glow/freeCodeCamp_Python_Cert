"""
Depth-first search (DFS) first goes down a path of edges as far as it can."""
# A stack is helpful in depth-first search algorithms because, as you add neighbors to the stack, you want to visit the most recently added neighbors first and remove them from the stack.
# A simple output of this algorithm is a list of nodes which are reachable from a given node. Therefore, you'll also want to keep track of the nodes you visit.

def dfs(adjacency_matrix, node_label:int):
    # create a stack and put the starting node inside it
    stack = [node_label]

    # create an empty list to keep track of nodes that we have visited
    visited = []

    # continue searching while there are nodes in the stack
    while stack:
        # remove the last node from the stack and store it as current
        current_node = stack.pop()

        # check if we already visited this node
        if current_node not in visited:
            # add this node to our visited list
            visited.append(current_node)

            # look at every possible neighbor of the current node 
            # adjacency_matrix[current_node] gives the row belonging to the current node
            for neighbor, connected in enumerate(adjacency_matrix[current_node]):
                # if there's an edge btwn the current node and this neighbor, add the neighbor to the stack so that DFS can visit it
                if connected == 1:
                    stack.append(neighbor)

    # return all nodes that were reachable from he node_label
    return visited