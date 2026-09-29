from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1: record frequencies in dict --> sort dict --> return top-k keys
        numFrequencies = defaultdict(int) # ie. {1:3, 2:2, 3:1}
        for x in nums:
            numFrequencies[x] += 1
        
        sorted_data = dict(sorted(numFrequencies.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_data.keys())[:k]

