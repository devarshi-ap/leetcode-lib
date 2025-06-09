class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bases = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            bases[sortedStr].append(s)
        
        return list(bases.values())
