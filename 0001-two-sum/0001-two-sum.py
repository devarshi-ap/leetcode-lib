class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Naive:
        - nested loop iter over nums and compare every (i, j) sum == target (i != j) 
        - O(n^2) because nested loop
        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and nums[i] + nums[j] == target:
                    return [i, j]