def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s=input("Enter a string:")
print ("The original string  is : ",end="")
print (s)
print ("The reversed string is : ",end="")
print (reverse(s))
if(s==reverse(s)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
"""
Enter a string:MOWA
The original string  is : MOWA
The reversed string is : AWOM
It is not a palindrome
"""
