class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # naive = 3 nested for-loops, exhaust all triplets (O(n^3))
        # a + b > c
        # l + r > c

        nums.sort()
        count = 0
        
        for i in range(len(nums)-1, 1, -1):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # satisfied, right-- to go to next class of possible triplets
                    count += right - left
                    right -= 1
                else:
                    # didn't satisfy, left++ to increase sum
                    left += 1
        return count
