#create a quewue data structure using list,which means first in first out(queue data structure)

queue=[]
while True:
    print("*"*45)
    print("\t1.Inserting value in queue")
    print("\t2.removing value from queue")
    print("\t3.Viewing queue")
    print("\t4.Exiting queue")
    print("*"*45)
    choice=int(input("Enter your choice : "))
    if choice == 1:
        value=int(input("enter your value:"))
        queue.append(value)
        print(f"value {value} inserted successfully")
    elif choice == 2:
        if len(queue)==0:
            print("queue is empty and nothing to do")
        else:
            num = queue[0]
            del queue[0]
            print(num,"deleted from queue")
    elif choice == 3:
        print(queue,"this is queue")
    elif choice == 4:
        break
    else:
        print("invalid Syntax")


        