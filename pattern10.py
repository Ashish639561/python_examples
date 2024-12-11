# for row in range(1,6):
#     for col in range(1,row+1):
#         print("*",end = " ")
#     print()


# for row in range(1,6):
#     for col in range(1,6):
#         if col == row:
#             print("* "* row,end = " ")
#     print()

# third method
for row in range(1,6):
    for col in range(1,6):
        if row >= col:
            print("*",end = " ")
    print()