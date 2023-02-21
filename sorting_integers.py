n=int(input("enter no of array elements"))
ar=[]
print("enter array elements:")
for i in range(n):
    arr=int(input(""))
    ar.append(arr)
print(ar)
l1=[]
l2=[]
for ele in ar:
    if ele >= 0:
        l1.append(ele)
    else:
        l2.append(ele)
L=l1+l2
print(L)
print("after sort")
L.sort()
print(L)
"""
OUTPUT:
enter no of array elements5
enter array elements:
1
4
5
7
-7
[1, 4, 5, 7, -7]
[1, 4, 5, 7, -7]
after sort
[-7, 1, 4, 5, 7]
"""
'''
strings = [str(integer) for integer in L]
a_string = "". join(strings)
an_integer = int(a_string)
print(an_integer)
'''