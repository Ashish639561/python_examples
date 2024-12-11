for row in range(5,0,-1):
    for col in range(1,row+1):
        if row % 2 == 0:
            print("$", end = " ")
        else:
            print("*", end = " ")
    print()

# method 2

for row in range(5,0,-1):
    for col in range(1,row+1):
        if row>=col:
            if row % 2 == 0:
                print("$", end = " ")
            else:
                print("*", end = " ")
    print()