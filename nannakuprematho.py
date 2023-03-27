def nannakuprematho (soldiers):
    nearest= 1
    while nearest*2 <= soldiers:
        nearest *= 2
    return (soldiers-nearest)*2+1

while(1):
    soldiers = int(input("enter no of soldiers:"))
    print("The person who is alive is:",nannakuprematho (soldiers))
