##average
numb = int(input("How many numbers do you have: "))
numbers =[]
while len(numbers) < numb:
       no = int(input("Give me your number: "))
       numbers.append(no)  
print(sum(numbers)/numb)