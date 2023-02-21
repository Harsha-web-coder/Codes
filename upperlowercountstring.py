def letters(str):
    lowercase=0
    uppercase=0
    for char in str:
        if(char.isupper()):
            uppercase+=1
        elif(char.islower()):
            lowercase+=1
    print("The number of uppercase letters in the given string is:",uppercase)
    print("The number of lowercase letters in the given string is:",lowercase)
name=input("Enter a string:")
letters(name)
