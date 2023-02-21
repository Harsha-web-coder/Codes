n=int(input("enter no of elements"))
l=[]
for i in range(n):
    a=int(input(""))
    l.append(a)
l.sort()
if n % 2 == 0:
    a=n//2
    median1 = l[a]
    median2 = l[a - 1]
    median = (median1 + median2)/2
else:
	median = l[n//2]
print(l)
while True:
    q=int(input(("enter\n1.for least element\n2.for middle element\n3.max element ")))

    if q==1:
        print("least Element is:",l[0])
    elif q==2:
        print("middle Elemnet is: ",median)
    else:
        print("Max Ele",l[n-1])

