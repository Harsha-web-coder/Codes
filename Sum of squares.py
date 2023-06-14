##Sum of squares

def sum_of_square2(n):
    sum = n*(n+1)*(2*n+1)/6
    return sum

num = int(input('Enter a number: '))
sum = sum_of_square2(num)
print('Your sum of Square is: ', sum)
