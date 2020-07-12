def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr) - 1

    while start < end:
        middle = start + (end - start)
        middle_item = arr[middle]
        
        if target == middle_item:
            return middle
            
        elif target < middle_item:
            end = middle - 1

            
                

    return -1  # not found
