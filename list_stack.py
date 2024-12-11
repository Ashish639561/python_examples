#create a stack data structure using list,which means last in first out(stack data structure)
list1=[]
while True:
    print("*"*45)
    print("\t1.Inserting value in stack")
    print("\t2.removing value from stack")
    print("\t3.view the stack ")
    print("\t4.exit")
    print("*"*45)
    choice=int(input("Enter your choice : "))
    match (choice):
        case 1:
            value=int(input("enter the value to insert : "))
            list1.append(value)
            print(list1)
        case 2:
            if len(list1)==0:
                print("stack is empty")
            else:
                num=list1.pop()
                print(num,"removed from stack")
        case 3:
            print("stack elements are : ",list1)
        case 4:
            break
        case _:
            print("Invalid choice")