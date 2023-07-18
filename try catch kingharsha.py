print("type harshaisking")
while True:
    try:
        age = input("Please enter: ")
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue 
    else:
        break
if age == "harshaisking":
        print("yes harsha is king!") 
else:
    print("You are a slave to harshaking")
    
