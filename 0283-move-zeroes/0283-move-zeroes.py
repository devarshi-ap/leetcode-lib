class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            left, right = 0, 1
            while right <= len(nums)-1:
                if nums[left]==0 and nums[right]!=0: # ie. 0, 1
                    nums[left], nums[right] = nums[right], nums[left] # swap
                    left += 1
                    right += 1
                elif nums[left]!=0 and nums[right]==0: # ie. 1, 0
                    left += 1
                    right += 1
                elif nums[left]!=0 and nums[right]!=0: # ie. 1, 1
                    left += 1
                    right += 1
                else: # ie. 0, 0
                    right += 1

# [4,2,4,0,0,3,0,5,1,0]
#  L R