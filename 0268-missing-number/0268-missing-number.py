class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        use: Sum[0...n] = [n(n+1)]/2
        """

        N = len(nums)
        expectedSum = (N * (N+1)) // 2
        actualSum = sum(nums)

        return expectedSum - actualSum