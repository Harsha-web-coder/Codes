n=int(input(""))
k=int(input(""))
l=[]
for i in range(n):
    a=int(input(""))
    l.append(a)
l.sort()
print(l[k-1])


"""
6
3
7
10
4
3
20
15
"""
