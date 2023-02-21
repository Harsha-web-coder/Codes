from collections import Counter
l = []
n =int(input("enter no of elements to be in a list:"))
for i in range(n):
    a=int(input(""))
    l.append(a)

x = int(input("enter a value to find occurences:"))
d = Counter(l)
if x in l:
    print('{} has occurred {} times'.format(x, d[x]))
else:
    print("elements not in the list provided")
"""
#we can also find max value occurences by finding the max element in the list
"""
x=max(l)
print("max element {} has occured {} times".format(x, d[x]))

"""
#we can also find max occuerences of a value in the list
"""
l1=[]
for i in range(n):
    l1.append(d[l[i]])
t=max(l1)
#print("element of {} has repeated max times".format(l[t]))
