class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ctr = Counter(nums)
        result = []
        while k > 0:
            currMaxKey = max(ctr, key=ctr.get)
            result.append(currMaxKey)
            del ctr[currMaxKey]
            k -= 1
        return result