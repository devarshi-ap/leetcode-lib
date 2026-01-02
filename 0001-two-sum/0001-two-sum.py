class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted = {}
        for i in range(len(nums)):
            iNeed = target - nums[i]
            if iNeed in wanted: # twoSum pair found
                return [wanted[iNeed], i]
            else: # not found (so make new wanted entry)
                wanted[nums[i]] = i
            print(wanted)

