
##gmail and password generator
import random
import string
 
first=input("Enter your First name: ")
last=input("Enter your Last name: ")
num=int(input("Enter your Password length: "))
 
all_chars = string.ascii_letters+string.digits+string.punctuation
 
email = first+ '.' + last + '@gmail.com'
password = ''
 
for i in range(num):
   rand_char=random.choice(all_chars)
   password = password + rand_char
 
print("Your Gmail Id: "+ email)
print("Your Password: "+ password)