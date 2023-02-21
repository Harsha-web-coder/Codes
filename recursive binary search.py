def binary_search(arr, low, high, x):
	if high >= low:

		mid = (high + low) // 2
		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		else:
			return binary_search(arr, mid + 1, high, x)

	else:

		return -1


arr=[]
n=int(input("enter number of elements in a list"))
for i in range(n):
    a=int(input(""))
    arr.append(a)
    
x = int(input("enter the element need to find"))

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
"""
recursive binary search
input:
enter number of elements in a list5
12
23
34
45
56
enter the element need to find34
output:
Element is present at index 2
"""
