def find_the_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def chose_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_the_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return(sorted_arr)

print(chose_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0, 24546, 56786, 2, 3224432]))
                

