class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallerN = min(len(str1), len(str2))
        gcdStr = ""
        for i in range(1, smallerN+1):
            if str1[:i] == str2[:i]:
                needed_for_One = len(str1) // i
                needed_for_Two = len(str2) // i
                print(str1[:i], needed_for_One, needed_for_Two)
                if str1[:i]*needed_for_One == str1 and str1[:i]*needed_for_Two == str2:
                    gcdStr = str1[:i]
        return gcdStr