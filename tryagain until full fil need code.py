while True:
    try:
        age = int(input("Please enter your age: ")) 
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break 
if age >= 18:
    print("You are able to vote!") 
else:
    print("You are not able to vote!")