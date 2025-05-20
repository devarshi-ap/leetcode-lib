class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # â = n(n + 1)/2
        N = len(nums)
        expectedSum = int(N * (N+1) / 2)
        actualSum = sum(nums)
        return expectedSum - actualSum