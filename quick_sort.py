def quick_sort(arr):
    if len(arr) < 2:
        return(arr)
    main_index = arr[0]
    left = [i for i in arr[1:] if i <= main_index]
    right = [i for i in arr[1:] if i > main_index]
    return quick_sort(left) + [main_index] + quick_sort(right)

print(quick_sort([10, 5, 2, 3]))