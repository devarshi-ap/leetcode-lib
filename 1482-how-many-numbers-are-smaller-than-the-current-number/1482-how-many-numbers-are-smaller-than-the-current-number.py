class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # naive = nested for loop (O(n^2))
        
        # "index of X in sorted array = how many value's are smaller than it
        # ie. index of 8 in [1,2,2,3,8] is 4 (larger than 4 others)"
        
        sorted_nums = sorted(nums) # [1,2,2,3,8]

        # {1:0, 2:1, 3:3, 8:4}
        lookup = {}
        for i, num in enumerate(sorted_nums):
            if num not in lookup:
                lookup[num] = i

        #[1,2,2,3,8] --> lookup --> [0,1,1,3,4]
        return [lookup[x] for x in nums]