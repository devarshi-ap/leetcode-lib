class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        pairs = 0

        while l < r:
            currSum = nums[l] + nums[r]
            if currSum == k: # hit, remove nums, move pointers in
                pairs += 1
                l += 1
                r -= 1
            elif currSum > k: # sum too high, move r down
                r -= 1
            else: # sum too low, move l up
                l += 1
        
        return pairs