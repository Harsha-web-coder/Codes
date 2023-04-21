x=int(input("Enter range of numbers:"))
[print("FizzBuzz") if (n %3 == 0) and (n % 5 ==0 ) else print("Fizz") if (n%3 == 0) else print("Buzz") if (n%5 == 0) else print(n) for n in range(1,x+1)]
