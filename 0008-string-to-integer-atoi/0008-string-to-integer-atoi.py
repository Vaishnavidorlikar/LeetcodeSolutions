class Solution:
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        sign = 1
        num = 0

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert digits
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Overflow check
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
