from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # {<sortedStr>: [anagrams, ...],}
        # Approach 1: sort str's, add to bin based on sorted-str key match, return values [O(nlogn) time, O(n) space]
        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagrams.setdefault(sortedWord, []).append(word)
        
        return list(anagrams.values())