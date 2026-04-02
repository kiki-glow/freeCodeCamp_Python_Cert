def quick_sort(array):
    if len(array) <= 1:
        return array[:]

    pivot = array[0]
    
    left = []
    right = []
    equal = []

    for element in array:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            equal.append(element)

    return quick_sort(left) + equal + quick_sort(right)         

if __name__ == "__main__":
    array = [4, 2, 7, 1]
    sorted_list = quick_sort(array)
    print(sorted_list)