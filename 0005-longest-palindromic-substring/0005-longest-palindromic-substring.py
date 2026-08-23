class Solution:
    def longestPalindrome(self, s: str) -> str:
        # sliding middle-out approach
        maxPal = ""

        for i in range(len(s)):
            # odd length expansion (l,r move outwards same pace)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]: # inbounds + chars match
                maxPal = max(maxPal, s[l:r+1], key=len)
                l -= 1
                r += 1
            
            # same, but now repeat for even length expansion (r=i+1 to begin)
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]: # inbounds + chars match
                maxPal = max(maxPal, s[l:r+1], key=len)
                l -= 1
                r += 1
        return maxPal
                