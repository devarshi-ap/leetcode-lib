class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for x in nums:
            if x in numsDict:
                return True
            else:
                numsDict[x] = 1
        return False