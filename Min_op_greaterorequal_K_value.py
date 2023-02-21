N=int(input("enter N value"))
K=int(input("enter K value"))
A=[]
count=0
for i in range(N):
    a=int(input(""))
    A.append(a)
A.sort()
if A[0]==K:
    print("0")
else:
    while A[0] <= A[1]:
        q=A[0]+A[1]
        A.pop(0)
        A.pop(0)
        A.insert(0,q)
        count+=1
    print(count-1)
"""
N = 4, K = 4
Arr[] = {5, 4, 6, 4}
Output: 0
Explanation: Every element in the given array 
is greater than or equal to K.
"""
"""
N = 6, K = 6 
Arr[] = {1, 10, 12, 9, 2, 3}
Output: 2
Explanation: First we add (1 + 2), now the
new list becomes 3 10 12 9 3, then we add
(3 + 3), now the new list becomes 6 10 12 9,
Now all the elements in the list are greater
than 6. Hence the output is 2 i:e 2 operations
are required to do this.
"""

