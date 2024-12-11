num=int(input("enter a number: "))
#a number is prime number when it is greater then 1 and only divisible by 1 and itself.ex->11 is divisible by only 1 and 11
#a number is a composite number when it has more then 1 divisor ex->24 is divide by 1,2,3,4,6,8,12 and 24
#1 is not a prime number nor a composite number
if num<=1:
    print(f'{num} not a prime number')
else:
    for i in range(2,num//2+1):#ex->33,so it would go so long for this we did 33//2+1 becuz in range 33-1=32 so 32//2=16+1->17
        if (num%i) == 0:
            print(f'{num} is not a prime number')
            print(f"it is divisible by {i}")
            break
    else:
        print(f'the {num} is a prime number')
