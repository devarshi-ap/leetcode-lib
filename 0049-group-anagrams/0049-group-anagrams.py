from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # {<sortedStr>: [anagrams, ...],}
        # Approach 1: sort str's [nlogn], map to dict based on sorted-str keys, return values [O(nlogn) time, O(n) space]
        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagrams.setdefault(sortedWord, []).append(word)
        
        # Approach 2: create letter-count vectors, map to dict, return values
        """
        ie. "tea" -> {[a:1, .., e:1, .., t:1, ...]} which acts as key in dict to actual words
        for word in strs:
            countMap = [0] * 26
            for letter in word:
                countMap[ord(letter) - ord("a")] += 1
            
            anagrams.setdefault(tuple(countMap), []).append(word)
        """

        return list(anagrams.values())