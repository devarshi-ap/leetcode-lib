class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bases = {}
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr not in bases:
                bases[sortedStr] = [s]
            else:
                bases[sortedStr].append(s)
        
        return list(bases.values())
