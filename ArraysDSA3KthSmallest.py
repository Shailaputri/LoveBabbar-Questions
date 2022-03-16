#Love Babbar Qns
print("\nArrays")
print("\nKth smallest element in an array")
A = [7,10,4,3,20,15]
B = A
N = len(A)
K = 3
new_A = A


def find_smallest(A):
	i = 1
	small_array = A[0]
	while i < len(A):
		if A[i] <= small_array:
			small_array = A[i]
		i += 1
	return small_array

def pop_smallest(A,s):
	i = 0
	while i < len(A):
		if A[i] == s:
			A.pop(i)
		i += 1	
	return A

i = 0

while i < K:
	small = find_smallest(new_A)
	new_A = pop_smallest(new_A,small)
	i += 1

print("{}th smallest element is : {}".format(K,small))


