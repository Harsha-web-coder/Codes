def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = []
n=int(input("enter number of elements in a list"))
for i in range(n):
    a=int(input(""))
    data.append(a)
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
"""
input:
enter number of elements in a list5
12
54
34
45
56
output:
Sorted Array in Ascending Order:
[12, 34, 45, 54, 56]
