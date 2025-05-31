class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        k = 1
        occurrence = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurrence += 1 # found pair, increase flag
            else:
                occurrence = 1 # not pair, reset flag
            
            if occurrence <= 2:
                nums[k] = nums[i]
                k += 1
        
        return k