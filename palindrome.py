##palindrome
my_str = input('String to check: ')
rev_str = my_str[::-1]

if my_str == rev_str:
  print("It is palindrome")
else:
  print("It is not palindrome")

##cube of num.
n = int(input('Enter a number: '))
sum = (n*(n+1)/2)**2
print('Your sum of cubes are: ', sum)