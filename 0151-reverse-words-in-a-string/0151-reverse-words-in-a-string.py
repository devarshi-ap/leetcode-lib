class Solution:
    def reverseWords(self, s: str) -> str:
        # Two Pointer Solution
        """
        l = r = len(s) - 1
        words = ""
        
        while r >= 0:
            if s[r] == " ":
                r -= 1
            else:
                l = r
                while l >= 0 and s[l] != " ":
                    l -= 1
                words += s[l+1:r+1]
                words += " " if l != 0 else ""
                r = l
        
        return words.strip()
        """

        # one-liner:
        return " ".join(reversed(s.split()))