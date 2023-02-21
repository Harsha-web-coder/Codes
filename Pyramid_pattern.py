rows=int(input())
for i in range(1,rows+1):
    for space in range(i, rows):
        print(" ",end="") 
    for j in range(1,2*i):
        if(i==j):
            print("B", end="")
        else:
            print("A", end="")

    print()
"""
4
   B
  ABA
 AABAA
AAABAAA
"""