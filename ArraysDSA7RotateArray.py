#Love Babbar Qns
print("\nArrays")
print("\nCyclically rotate array by 1")
array = [1,2,0,-1,2,5]
#[1,2,3,4,5]

def rotate(A,S="Clock"):
	if S == 'Anti':
		i = 0
		temp = A[0]
		while i < len(A)-1:
			print("Ok")
			A[i] = A[i+1]
			i += 1
		A[-1] = temp
		print(A)
	else:
		i = len(A)-1
		temp = A[-1]
		while i > 0:
			print("Ok")
			A[i] = A[i-1]
			i -= 1
		A[0] = temp
		print(A)

rotate(array)
