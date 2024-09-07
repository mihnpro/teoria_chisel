def binary_search(sorted_arr, num):
    f = 0
    index = 0
    while (f == 0):
        left = sorted_arr[len(sorted_arr) // 2]
        right = sorted_arr[len(sorted_arr) // 2 - 1]
        print(left, right)
        if (num < left):
            sorted_arr = sorted_arr[:left+1]
            index = index + left
        elif (num > right):
            sorted_arr = sorted_arr[right:]
            index = index + right
        
        if (num == left):
            f = 1
            index = left - 1
            return index, "left"
        elif (num == right):
            f = 1 
            index = right - 1
            return index, "right"
print(binary_search([i for i in range(1, 10001)], 6549))

