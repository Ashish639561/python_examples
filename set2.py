a={40,60,90,25,75,100,"ashish"}
b={40,60,75,90,25,64,264,89}
c={755,986,45,785,87}
print("1\t",a.union(b))
print(a|b)#union and | both are used for same
print("2\t",a.intersection(b))
print("3\t",a.difference(b))
print("4\t",a.difference(c))
print("5\t",a.difference(b,c))#here it will take all the union of b and ac then differnciate
print("6\t",a.issuperset(b))
print("7\t",b.issubset(a))
print("8\t",a>=b)#we can use >= for superset
print(b<=a)#<= for subset
print(a.symmetric_difference(b))#combine from both set and gives new set which are not in set and set 2
print(a.isdisjoint(b))#returns true if both sets don't have common value otherwise false
print(a)
print(b)
str1="mmmmTHISis python classnnn"
print(str1.strip('m'))
print(str1.casefold())
