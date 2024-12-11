for row in range(1,6):
    for col in range(1,6):
        if col == row:
            if row % 2==0:
                print("$ "*row,end =" ")
            else:   
                print("* "*row,end =" ")
    print()    

print("-"*40)
            
for row in range(1,6):
    for col in range(1,row+1):
        if row % 2==0:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

print("-"*40)

for row in range(1,6):
    for col in range(1,6):
        if row >=col:
            if row % 2==0:
                print("$",end=" ")
            else:
                print("*",end=" ")
    print()
