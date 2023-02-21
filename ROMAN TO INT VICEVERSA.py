def printRoman(number):
	num = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
	sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
	i = 12
	
	while number:
		div = number // num[i]
		number %= num[i]
		while div:
			print(sym[i], end = "")
			div -= 1
		i -= 1

if __name__ == "__main__":
	number = int(input("enter any integer to convert into romans:"))
	print("ROMAN VALUE:", end = " ")
	printRoman(number)
def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	if (r == 'L'):
		return 50
	if (r == 'C'):
		return 100
	if (r == 'D'):
		return 500
	if (r == 'M'):
		return 1000
	return -1

def romanToDecimal(str):
	res = 0
	i = 0
	while (i < len(str)):
		s1 = value(str[i])

		if (i + 1 < len(str)):
			s2 = value(str[i + 1])
			if (s1 >= s2):
				res = res + s1
				i = i + 1
			else:
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1
	return res
a=input("\nenter any roman value:")
print("INTEGER VALUE:",romanToDecimal(a))