def count_palindromes(S):
	def check(l, r, S, count):
		print(id(count))
		while l >= 0 and r < len(S) and S[l] == S[r]:
			l -= 1
			r += 1
			count = count + 1
	count = 0
	for idx, i in enumerate(S):
		print(id(count))
		check(idx, idx+1, S, count)
		check(idx, idx, S, count)
	return count
	
s = 'hellolle'
s = 'wowpurerocks'
print(count_palindromes(s))