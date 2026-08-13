class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # naive
        """
        expected = {i: i for i in range(1, len(nums)+1)}
        print(expected)

        for x in nums:
            expected.pop(x, None)
        
        return list(expected.keys())
        """

        # optimize and use sets:
        expected = [i for i in range(1,len(nums)+1)] # [1, 2]
        setNums = set(nums) # [1]
        return [x for x in expected if x not in setNums] # missing [2]
