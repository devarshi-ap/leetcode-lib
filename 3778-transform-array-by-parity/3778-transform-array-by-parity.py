class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        modArr = [x % 2 for x in nums]
        modArr.sort()
        return modArr