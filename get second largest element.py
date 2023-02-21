#printing second larget element in a list
print("Enter the numbers as comma seperated: ")
l1=[]
inp = list(map(int, input().split(",")))
for i in range(len(inp)):
    for j in range(len(inp)):
        l=inp[j]-inp[i]
        if l>0:
            l1.append(l)
print(max(l1))
