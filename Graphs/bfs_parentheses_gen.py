"""
Implement a function that generates all valid combinations of parentheses using a breadth-first search (BFS) approach."""

def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be at least 1'
    
    # create a queue containing the starting state as a tuple. 
    # the tuple contains 
    # '' -> the current parentheses string 
    # 0 -> number of opening parentheses used 
    # 0 -> number of closing parentheses used
    queue = [('', 0, 0)]
    # create an empty list to store valid combos
    result = []

    # continue running while the queue is not empty
    while queue:
        print(queue)
        current, opens_used, closes_used = queue.pop(0)
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))
    
    return result

print(gen_parentheses(2))
print(gen_parentheses(3))