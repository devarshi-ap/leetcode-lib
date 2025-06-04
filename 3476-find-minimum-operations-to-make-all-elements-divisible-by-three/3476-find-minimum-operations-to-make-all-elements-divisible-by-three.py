class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numOps = 0
        for x in nums:
            if (x-1) % 3 == 0 or (x+1) % 3 == 0:
                numOps += 1
        return numOps