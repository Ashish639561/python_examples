str1="fadefad"#fadefad this is for odd and #amaama this is for even
if len(str1)%2==0: #checkimg for even length
    if str1[:len(str1)//2] == str1[len(str1)//2:]:
        print(str1,"for even symmetrical")
    else:
        print(str1,"not even symmetriacl")
else:
    if str1[:len(str1)//2] == str1[len(str1)//2+1:]:
        print(str1,"for odd symmete")
    else:
        print("not odd symm")

if str1[:] == str1[::-1]:
    print(str1,"is palindrome")
else:
    print(str1,"is not palindrome")