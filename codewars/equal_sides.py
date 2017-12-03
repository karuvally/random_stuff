def find_even_index(arr):
    # if array is empty, return 0
    if len(arr) == 0:
        return 0

    # the main loop begins
    for i in range(0, len(arr)):
        # initialize the values
        left_sum = 0
        right_sum = 0
        
        # calculate sum to the left of index
        for j in range(0, i):
            left_sum += arr[j]
        
        # calculate sum to the right of index
        for k in range(i+1, len(arr)):
            right_sum += arr[k]
        
        # return index if it satisfies condition
        if left_sum == right_sum:
            return i
    
    # if no index can be found, return -1
    return 1
