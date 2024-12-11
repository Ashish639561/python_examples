# Input : str =" geeks quiz practice code"
# Output : str = "code practice quiz geeks" 

str1 = "geeks quiz practice code"
print(str1)
print(len(str1))
list1=str1.split()
str2=" ".join(list1[::-1])
print(str2)
print(len(str2))
