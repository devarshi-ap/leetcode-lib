class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0

        while i < len(word1) and i < len(word2): # exhaust i until shorter word exhausted
            result += word1[i]
            result += word2[i]
            i += 1
        
        # now add rest from both words (shorter word returns "")
        result += word1[i:] + word2[i:]

        return result