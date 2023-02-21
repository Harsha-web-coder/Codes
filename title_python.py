n=input("")
l=n.split(" ")
n=len(l)
for i in range(n):
    s=l[i][0].upper()
    x=str(s+l[i][1:])
    print(x,end=" ")
