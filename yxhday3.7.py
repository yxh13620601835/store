'''
    编程实现下列图形的打印7*7
            *
           *  *
          *  *  *
         *  *  *  *
        *  *  *  *  *
    author:yxh
'''
for i in range(0,7):
    for j in range(0,7-i):
        print(end=" ")
    for k in range(7-i,7+1):
        print("*", end=" ")
    print()