

def insertion_sort(arr=[]):
	for i in range(len(arr)):
		key = arr[i]
		lo, hi = 0, i - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if key < arr[mid]:
				hi = mid
			else:
				lo = mid + 1

		for j in range(i, lo + 1, -1):
			if (j == 0):
				if (arr[i] < arr[j]):
					(arr[i], arr[j]) = (arr[j], arr[i])
			else:
				print(f"j={j} i={i} lo={lo}")
				arr[j] = arr[j - 1]
			
		arr[lo] = key
		
	return arr

#print(insertion_sort([1,32,3]))
print(insertion_sort([4,32,3, 5, 7]))