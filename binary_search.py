def binary_search(sorted_arr, num):
    low = 0
    hight = len(sorted_arr) - 1
    while (hight >= low):
        print(low, hight)
        mid = hight + low
        guess = sorted_arr[mid]
        if num == guess:
            return mid
        elif guess > num:
            hight = mid -1 
        else:
            low = mid - 1
    return None
print(binary_search([1, 4, 8, 10, 19, 8765, 876543456], 8765))

