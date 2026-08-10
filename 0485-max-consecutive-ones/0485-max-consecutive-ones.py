class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currSum, maxSum = 0, 0
        for x in nums:
            if x == 1:
                currSum += 1
            else:
                maxSum = max(maxSum, currSum) # update max
                currSum = 0
        return max(maxSum, currSum) # final update max