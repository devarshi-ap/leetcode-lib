class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # naive = nested for loop (O(n^2))
        
        # sorted array's index of X is how many value's are smaller than it
        
        return [sorted(nums).index(x) for x in nums]