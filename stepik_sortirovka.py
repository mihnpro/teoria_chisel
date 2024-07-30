a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(a)
for i in range(n):
    maxx = a[0]
    for j in range(n-i):
        if maxx <= a[j]:
            j_max = j
    for k in range(j_max, n-i-1):
        a[k], a[k+1] = a[k+1], a[k]


print(a)