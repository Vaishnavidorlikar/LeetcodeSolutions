class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # palindrome length

        for i in range(len(s)):
            len1 = expand(i, i)       # odd length
            len2 = expand(i, i + 1)   # even length

            curr_len = max(len1, len2)

            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2

        return s[start:start + max_len]
