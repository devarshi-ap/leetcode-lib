class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value:index_found_at
        
        for i, x in enumerate(nums):
            need = target - x # 7 = 9-2
            if need in seen: # is 7 in {}
                return [seen[need], i]
            else:
                seen[x] = i # {2:0} if anyone needs a 2, it's found at index 0
