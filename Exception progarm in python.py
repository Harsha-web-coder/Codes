s = input("enter an integer")
try:
    i = int(s)
    print("you entered",i)
except ValueError as err:
    print(err)