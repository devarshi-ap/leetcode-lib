from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1: sort str's, add to bin based on sorted-str key match, return values [O(nlogn) time, O(n) space]
        anagrams = {} # {<sortedStr>: [anagrams, ...],}

        for word in strs:
            # print(word, ''.join(sorted(word)))
            anagrams.setdefault(''.join(sorted(word)), []).append(word)
        
        return list(anagrams.values())