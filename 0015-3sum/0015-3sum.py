class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeroSumTriplets = []
        nums.sort()
        for i in range(len(nums)-2):
            
            # move i if next number is same (avoids dupes)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # init two pointers
            left, right = i+1, len(nums)-1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum > 0:
                    # too much --> dec. sum (R--)
                    right -= 1
                elif currSum < 0:
                    # too little --> inc. sum (L++)
                    left += 1
                else:
                    # match
                    zeroSumTriplets.append([nums[i], nums[left], nums[right]])

                    # move left in until new num (avoids dupes)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # ^ for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # triplet was added, move left & right in
                    left += 1
                    right -= 1
    
        return zeroSumTriplets