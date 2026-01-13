from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freqMap = defaultdict(int)
        for x in nums:
            freqMap[x] += 1
        
        for x in freqMap:
            if freqMap[x] != 2:
                return x