#Love Babbar Qns
print("\nArrays")
print("\nKadane Algo : Max sum of sub-array")
A = [-1,-2,-3]
#[1,2,3,-2,5]
N = len(A)
j = 0
C = []
#print(A[2:3])
while j<N:
	i = 0
	while i<N:
		if A[j:N-i] == []:
			break
		else:
			#print ("i,j and sub-array is are: {}, {}, {}".format(i,j,A[j:N-i]))
			#print(A[j:N-i])
			C.append(sum(A[j:N-i]))
			i += 1
	j += 1
print("Maximum sum of sub-array is : {}".format(max(C)))
'''
possibilities:
sum(A[0:N-0]) --> Full
sum(A[0:N-1]) --> Upto -2
sum(A[0:N-2]) --> Upto 3
sum(A[0:N-3]) --> Upto 2
sum(A[0:N-4]) --> only 1st element
sum(A[1:N-0])'''