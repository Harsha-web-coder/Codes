##armstrong strong no.~~2
#enter a number to verify that if its any armstrong number or not
def num_slicing(n):
   l = []
   while n > 0:
       l.append(n%10)
       n = n//10
   l.reverse()
 
   su = 0
   li_len = len(l)
   for i in l:
       res = i**li_len
       su += res
 
 
   su2 = ""
 
   for a in l:
       su2 = su2 + str(a)
 
   if su2 == str(su):
       print(su2, "is an armstrong number")
   if su2 != str(su):
       print(su2, "is not an armstrong number")
   return "we did it!!"
 
n = int(input("enter integer number: "))
print(num_slicing(n))