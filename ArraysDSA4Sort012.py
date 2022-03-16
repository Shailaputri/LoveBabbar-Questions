#Love Babbar Qns
print("\nArrays")
print("\nArray of 0 1 2")
A = []
B = []
C = []
S = [0,1,2,2,1,1,0,0,1,2]
#[0,2,1,2,0]
i = 0
while i < len(S):
	if S[i] == 0:
		A.append(S[i])
	elif S[i] == 1:
		B.append(S[i])
	else:
		C.append(S[i])
	i += 1
print(A+B+C)
