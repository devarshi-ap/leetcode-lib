class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0

        while i < min(len(word1), len(word2)): # 0 1
            result += word1[i]
            result += word2[i]
            i += 1
        
        # apbq, now add rs from longer word2
        result += word1[i:] if len(word1) > len(word2) else word2[i:]

        return result