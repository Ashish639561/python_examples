#this is done by me....
#writ a program to remove all duplcates of 1 using first approach
# list1=[1,2,3,4,5,1,2,4,1]
# c = list1.count(1)
# print(c)
# for _ in range(c):
#     list1.remove(1)
# print(list1)

#writ a program to remove all duplcates of 2 using second approach
list1=[1,2,3,4,5,1,2,4,1]
while True:
    if 2 in list1:
        list1.remove(2)
    else:
        break
print(list1)


#write a program to remove all duplicates of which includes in the list

# list2=[1,2,3,4,5,1,2,4,1,6,7,8,9,10,1,2,3,4,5]
# for value in list2:
#     c=list2.count(value)
#     for i in range(c-1):
#         list2.remove(value)
# print(list2)

#write a program to remove all duplicates of which includes in the list using your technique   
# list2=[1,2,3,4,5,1,2,4,1,6,7,8,9,10,1,2,3,4,5]             
# list2=list(set(list2)) 
# print(list2)     
# write a program to remove all duplicates of which includes in the list using your technique  


        