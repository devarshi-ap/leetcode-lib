from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # countMap -> anagrams[]
        for x in strs:
            countMap = [0] * 26 # a ... z
            for c in x:
                # ie. "abba" = [2a, 2b, 0c, ..., 0z]
                countMap[ord(c) - ord("a")] += 1
                
            groups[tuple(countMap)].append(x) # {[2a, 2b, 0c, ..., 0z]: [abba, baba, ...]}
        return list(groups.values())

