class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)

        # skip leading whitespace only
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        # determine sign
        sign = 1
        if s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # build number one digit at a time (int() only ever sees a single char)
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i]) # Mathematical way of iteratively reading number from L->R
            i += 1

        result *= sign

        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        return max(MIN_INT, min(MAX_INT, result))