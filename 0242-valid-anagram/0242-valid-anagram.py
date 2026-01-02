from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = Counter(s)

        for x in t:
            if x not in sFreq or sFreq[x] == 0:  # not anagram (must have same chars)
                return False
            else:
                sFreq[x] -= 1 # reduce matched-char count
                if sFreq[x] == 0:
                    del sFreq[x]
        
        return True if len(sFreq) == 0 else False

        