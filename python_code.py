def prime(num):
    flag=0
    for i in range(2,num//2 + 1):
        if num%i == 0:
            flag=1
            break
    if flag == 0:
        return 1
    else:
        return 0
def print_alt_prime(n):
    counter=0
    for num in range(2,n):
        if prime(num) == 1:
            if counter%2 == 0:
                print(num,end=" ")
            counter+=1
n=int(input())
print(print_alt_prime(n))