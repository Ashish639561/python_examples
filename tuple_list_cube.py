# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]

list1=[1,2,3]
list_output=[]
for num in list1:
    list_output.append((num, num**3))
print(list_output)

list2=[9,5,6]
list_output1=[(num,pow(num,3)) for num in list2]
print(list_output1)
print(pow(2,3))