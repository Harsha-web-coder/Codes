n=int(input("Enter a range:"))
num=int(input("Enter a number:"))
def rangeof(num):
    if num in range(1,n+1):
        print( " %s is in the range"%str(num))
    else :
        print("The number is outside the given range.")
rangeof(num)



