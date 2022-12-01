def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			
			return
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")



# def quick_sort(sequence):
#     length = len(sequence)
#     if length<= 1:
#         return sequence
#     else:
#         pivot = sequence.pop()


#     items_greater = []
#     items_lower = []

#     for item in sequence:
#         if item > pivot:
#             items_greater.append(item)

#         else:
#             items_lower.append(item)


#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# print(quick_sort([3,6,8,3,7,6,0,3,1,8,0,9,5,3,4]))