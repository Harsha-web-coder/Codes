for i in range(1,101):
    if i>1:
        for j in range(2,i): #(2,5) 
            if i%j== 0: #5%2 == 0
                print(i, "is not a prime number")
                break
        else:
            print(i, "is a prime number")