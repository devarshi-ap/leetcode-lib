class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0

        while i < min(len(word1), len(word2)): # 0 1
            result += word1[i]
            result += word2[i]
            i += 1
        
        # apbq, now add rs from longer word2

        if len(word1) > len(word2):
            # word1 is longer, add its rest to result
            result += word1[i:]
        else:
            result += word2[i:]

        return result