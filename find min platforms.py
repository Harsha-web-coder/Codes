def mowaPlatform(arr, dep, n):
	plat_needed = 1
	result = 1

	for i in range(n):
		plat_needed = 1

		for j in range(i+1, n):
			if (max(arr[i], arr[j]) <= min(dep[i], dep[j])):
				plat_needed += 1

		result = max(result, plat_needed)

	return result

def main():
	arr = [900, 915, 1030, 1045]
	dep = [930, 1300, 1100, 1145]

	n = len(arr)

	print("{}".format(mowaPlatform(arr, dep, n)))

if __name__ == '__main__':
	main()
