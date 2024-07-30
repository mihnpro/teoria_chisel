
#def prosto(f):
    #flag = 0
    #for i in range(2, f):
        #if f % i != 0:
            #flag = 1
            #break
    #if flag == 1:
        #return(False)
    #else:
        #return(True)


def is_prime(f):
    for i in range(2, (f//2)+1):
        if f % i == 0:
            return False
    return True


def make_pairs(n):
    s = [i for i in range(1, 2* n + 1)]
    arr_res = []
    arr_trash = []
    for i in range(1, len(s)):
        t = []
        for j in range(0, i):
            f = s[i] + s[j]
            if is_prime(f) == True and s[i] not in arr_trash and s[j] not in arr_trash:
                t.append(s[i])
                t.append(s[j])
                t = tuple(t)
                arr_res.append(t)
                arr_trash.append(s[i])
                arr_trash.append(s[j])

                break

    print(arr_res)


make_pairs(10)
