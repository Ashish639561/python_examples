str1="hello world"
# print(str1.replace("l","",1))
#this was first approach

print(str1)
#now second approach
# lst=[]
# for ch in str1:
#     if ch!="o":
#         lst.append(ch)
# print(lst)
# str="".join(lst)
# print(str)

#third approach of using list comprehension
lst2="".join([ch for ch in str1 if ch !="o"])
print(lst2)