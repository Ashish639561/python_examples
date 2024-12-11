# for row in range(5,0,-1):
#     for col in range(1,row+1):
#         print(row,end='')
#     print()

# print("-"*40)

# for row in range(5,0,-1):
#     for col in range(1,6):
#         if col<=row:
#             print("*",end="")
#     print()

# print("-"*40)

# for row in range(5,0,-1):
#     for col in range(1,6):
#         if col<=row:
#             print(row,end="")
#     print()

# print("*"*40)

for row in range(5,0,-1):
    for col in range(1,6):
        if col==row:
            print("*"*row,end="")
    print()
