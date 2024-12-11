"""glo=200
def outer():
    loc=100
    print(loc)
    print(glo)
    def inner():
        loc1=50
        nonlocal loc
        global glo
        print(loc1,loc,glo)
        loc=700
        glo=900
    inner()
    print(loc)
    print(glo)
print(glo)
outer()
print(glo)"""
start=10
end=20
l=[]
for i in range(start,end+1):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            l.append(i)
print(l)
"""
n=19
value=0
for i in range(2,n):
    if n%i==0:
        value=value+1
        break
if value==0:
    print(n,"is prime")
else:
    print("not prime")"""

        
    
