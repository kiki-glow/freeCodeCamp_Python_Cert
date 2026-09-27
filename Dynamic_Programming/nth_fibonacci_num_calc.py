def fibonacci(n):
    # create a sequence/list containing the first two Fibonacci numbers
    sequence = [0, 1]

    # keep calculating until the list contains n + 1 numbers   
    while len(sequence) <= n:
        # add the previous two numbers together to get the next number
        next_number = sequence[-1] + sequence[-2]

        # add the newly calculated number to the sequence list
        sequence.append(next_number)
    
    # return the nth Fibonacci number
    return sequence[n]
    
print(fibonacci(55))