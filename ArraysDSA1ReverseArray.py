#Love Babbar Qns
print("\nArrays")
print("\nReverse the array")
print("\nUsing iteration using another variable:")
s = 'Hello There'
i = 0
str_len = len(s)
m = []

while i<str_len:
	m.append(s[str_len - i-1])
	i = i+1
print(''.join(m))

print("\nUsing iteration wo using another variable:")
start = 0
end = len(m)-1
while start < end:
	m[start],m[end] = m[end],m[start]
	start += 1
	end -= 1
print(''.join(m))

print("\nWo Iteration :")
ans = s[::-1]
print(ans)





