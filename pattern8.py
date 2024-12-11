# for row in range(1,6):
#     for col in range(1,row+1):
#         print(row,end =" ")
#     print()

#another way to do this

for row in range(1,6):
    for col in range(1,6):
        if row>=col:
            print(row,end =" ")
    print()