# for row in range(1,6):
#     for col in range(1,6):
#         if row % 2 == 0:
#             print(0, end=' ')
#         else:
#             print(1, end=' ')
#     print()

#second way of doing this 

for row in range(5,0,-1):
    for col in range(1,6):
        if row % 2 == 0:
            print(0,end = " ")
        else:
            print(1,end = " ")
    print()