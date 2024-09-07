def a1_thick_and_hearty(a1, a2):
    var = set(a1) & set(a2)
    lenth1 = len(a1)
    lenth2 = len(a2) 
    res = []
    var = list(var)
    for i in range(len(var)):
       for j in range(0, i):
           
           if var[i] + var[j] == lenth1 or var[i] + var[j] == lenth2 or var[i] - var[j] == lenth1 or var[i] - var[j] == lenth2: 
               print(var[i], var[j])
               res.append(var[i])
               res.append(var[j])
    print(set(res))
        
a1_thick_and_hearty([1, 2, 3, 5, 10, 15], [1, 2, 3, 4, 5, 6, 10, 12, 15, 16])
                