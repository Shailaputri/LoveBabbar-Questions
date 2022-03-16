#Love Babbar Qns
print("\nArrays")
print("\nMax Min in an array")
A = [5]
#[5,6,3,7,2,9]
array_len = len(A)
i = 1
array_max = A[0]
array_min = A[0]
while i < array_len:
	if A[i] <= array_min:
		array_min = A[i]
		i += 1
	elif A[i] >= array_max:
		array_max = A[i]
		i += 1
	else:
		i += 1

print("\nThe maximum in array is: {}".format(array_max))
print("\nThe minimum in array is: {}".format(array_min))




