def unboxing(boxes):
    unbox = 0
    while unbox != "key":
       for i in range(len(boxes)):
        unbox = boxes[i][0]

       

print(unboxing([[[]], [[[]]], [[[[[[]]]]]], [[[[[["key"]]]]]] ]))
        
