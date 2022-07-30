class Solution(object):
	def longestPalindrome(self, s):
		n = len(s)
		i = 0
		substring = ""
		while i < n:
			l = i
			r = i
			while l >= 0 and r < n and s[l] == s[r]:
				l -= 1
				r += 1
			l += 1
			r -= 1
			if r - l + 1 > len(substring):
				substring = s[l: r + 1]
			l = i
			r = i + 1
			while l >= 0 and r < n and s[l] == s[r]:
				l -= 1
				r += 1
			l += 1
			r -= 1
			if r - l + 1 > len(substring):
				substring = s[l: r + 1]
			i += 1
		return substring
