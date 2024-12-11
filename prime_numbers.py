# Program to check if a number is prime or not
num = 24

#To take input from the user
#num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
      is_prime=True
      # check for factors
      for i in range(2, num//2+1):# 1,[2,3,4,5,6,7,8,9,10],11
        if (num % i) == 0:
            # if factor is found, set is_prime to False
            is_prime = False
            # break out of loop
            break

      # check if is_prime is True
      if is_prime == True:
        print(num, "is a prime number")
      else:
        print(num, "is not a prime number")
         
