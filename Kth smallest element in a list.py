l=[]
n1=int(input("enter kth place:"))
n=int(input("enter num of elements:"))
for i in range(n):
    a=int(input())
    l.append(a)
l.sort()
#print("yourlist after sort:",l)
print("your kth smallest val:",l[n1-1])
"""
output:
enter kth place:2
enter num of elements:5
3
4
2
5
1
your kth smallest val: 2
"""
