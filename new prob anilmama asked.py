while True:
    try:
        miles = float(input("Enter distance in miles: "))
    except ValueError:
        print("Sorry,I didn't understand that.Please enter correctly again.")
        continue
    else:
        break 
if miles >0:
	kilometers = miles*1.609344
	print("Distance in Kilometers:", kilometers)