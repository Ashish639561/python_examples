# num=5
# for row in range(1,6):
#     for column in range(1,6):
#         print(num,end="")
#     num=num-1
#     print()

# we can create this pattern with different methods also

for row in range(5,0,-1):
    for column in range(1,6):
        print(row,end="")
    print()