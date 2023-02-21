x="Gold Medal"
y="Silver Medal"
z="Bronze Medal"
l=[]
v=[]
n=int(input("enter number of players:"))
print("enter scores:")
for i in range(n):
    a=int(input(""))
    l.append(a)
    v.append(a)
l.sort(reverse = True)
print(v)

r=v.index(l[0])
f=v.index(l[1])
g=v.index(l[2])
v[r]=x
v[f]=y
v[g]=z
print(v)
"""
replace top max scores with repective medals

input:
enter number of players:5
enter scores:
10
3
8
9
4

output:
[10, 3, 8, 9, 4]
['Gold Medal', 3, 'Bronze Medal', 'Silver Medal', 4]
"""
