#Love Babbar Qns
print("\nArrays")
print("\nNegative elements in one side of array")
S = [-12,11,-13,-5,6,-7,5,-3,-6]
A = []
B = []
for ele in S:
	if ele < 0:
		A.append(ele)
	else:
		B.append(ele)
print(A+B)
