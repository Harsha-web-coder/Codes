print("Enter the String: ")
str = input()

print("Enter a character: ")
char = input()

newstr = ""
for i in range(len(str)):
    if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
        newstr = newstr + char
    else:
        newstr = newstr + str[i]

print("\nOriginal String:", str)
print("New String:", newstr)
