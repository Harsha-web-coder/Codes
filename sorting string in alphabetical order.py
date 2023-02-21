a=input("enter a string:")
l=[]
s=""
for i in range(len(a)):
    l.append(a[i])
l.sort()
for i in range(len(l)):
    s+=l[i]
print("after soring string:",s)
"""
sorting string in alphabetical order
input:
enter a string:harsha
output:
after soring string: aahhrs
"""
