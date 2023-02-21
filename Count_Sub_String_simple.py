test_str = input("")
sub = input("")
#print("The original string is : " + str(test_str))
res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]

#print("substrings: " + str(res))
n=len(res)
#print(res[0])
#print(n)
count=0
for i in range(n):
    if res[i]==sub:
        count+=1
print(count)
