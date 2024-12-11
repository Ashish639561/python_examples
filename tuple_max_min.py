#find 2 max numbers and find 2 min numbers
test_tup = (3, 7, 1, 18, 9)
k = 2 
#using first approach sorted functions to convert tuplesinto list beccause tuple doesn't have sort function
test_tuples=sorted(test_tup) 
print(test_tuples)          
min_tup = test_tuples[:k]
max_tup = test_tuples[-k:]
total_tup=tuple(min_tup+max_tup)
print(total_tup)

#using second approach without using sorted function
first_max_num=float('-inf')
second_max_num=float('-inf')
first_min_num=float('inf')
second_max_num=float('inf')

for num in test_tup:
    if num>first_max_num:
        second_max_num=first_max_num
        first_max_num=num
    elif num>second_max_num:
        second_max_num=num
    
    if num<first_min_num:
        second_min_num=first_min_num
        first_min_num=num
    elif num<second_min_num:
        second_min_num=num
result=(first_min_num, second_min_num, second_max_num, first_max_num)
print(result)

#find 1 max and min number of tuples

test_tup1=(3,7,1)
k1=1

test_tup1=sorted(test_tup1)

min_tuple1=test_tup1[:k1]
max_tuple1=test_tup1[-k1:]
total_list1=min_tuple1+max_tuple1
print(tuple(total_list1))



