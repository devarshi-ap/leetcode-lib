from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create freq map
        freqMap = defaultdict(int)
        for x in nums:
            freqMap[x] += 1
        
        # bucketing (index = freq)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for val,freq in freqMap.items():
            buckets[freq].append(val)
        
        # get top k from buckets (count backwards until k-elements are collected)
        results = []
        for i in range(len(buckets)-1, -1, -1):
            for x in buckets[i]:
                if len(results) < k:
                    results.append(x)
                else:
                    break
        return results

