#Love Babbar Qns
print("\nArrays")
print("\nMin no of jumps")
A = [1, 3, 0, 8, 9, 2, 6, 7, 6, 8, 9]
#[1,9,3,2,6,7]
N = len(A)
i = 0
count = 0
while i<N:
	if A[i] == 0:
		print ("Cannot reach end of array")
		count = 'Invalid'
		break
	else:
		i = i+A[i]
		count = count+1

print("Number of jumps to reach of array is {}".format(count))
