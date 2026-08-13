class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        expected = {i: i for i in range(1, len(nums)+1)}
        print(expected)

        for x in nums:
            expected.pop(x, None)
        
        return list(expected.keys())