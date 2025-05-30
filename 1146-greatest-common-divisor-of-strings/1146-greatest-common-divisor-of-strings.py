class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallerN = min(len(str1), len(str2))
        gcdStr = ""
        i = 1
        while i < smallerN+1:
            if str1[:i] == str2[:i]:
                if str1[:i]*(len(str1) // i) == str1 and str1[:i]*(len(str2) // i) == str2:
                    gcdStr = str1[:i]
            i += 1
        return gcdStr