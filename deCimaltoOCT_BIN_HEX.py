def decbi(n):
    k=0
    q=0
    while(n!=0):
        r=n%2
        n=n//2
        q+=r*(10**k)
        k+=1
    return q
n=int(input("Enter decimal value:"))
print("Binary number for  a given decimal number is:",end=" ")
print(decbi(n))
def decoct(n):
    k=0
    q=0
    while(n!=0):
        r=n%8
        n=n//8
        q+=r*(10**k)
        k+=1
    return q

print("Octal number for  a given decimal number is:",end=" ")
print(decoct(n))
def dechex(n):
    k=0
    q=0
    while(n!=0):
        r=n%16
        n=n//16
        q+=r*(10**k)
        k+=1
    return q

print("Hexadecimal number for  a given decimal number is:",end=" ")
print(dechex(n))
