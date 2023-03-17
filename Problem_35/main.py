def d(a, b):
	return 1 - int(a == b)

def L(s, t):
	dict_memoization = {}
	def recursion(s, t):
		len_s = len(s)
		len_t = len(t)
		key = (s, t)
		if len_s == 0:
			return len_t
		elif len_t == 0:
			return len_s
		elif key in dict_memoization:
			return dict_memoization[key]
		else:
			dict_memoization[key] = min(
				recursion(s[:-1], t) + 1,
				recursion(s, t[:-1]) + 1,
				recursion(s[:-1], t[:-1]) + d(s[-1], t[-1])
			)
			return dict_memoization[key]
	return recursion(s, t)

def main():
	l = L("123456789", "123abc")
	print(l)

main()

