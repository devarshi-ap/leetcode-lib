class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # A) In-Place Negative Marking Approach
        dupe, lost = 0, 0

        for x in nums:
            idx = abs(x)
            if nums[idx-1] < 0: # negative; already marked
                dupe = idx # found dupe
            else:
                nums[idx-1] = -nums[idx-1] # mark -x
        
        for i, x in enumerate(nums):
            if x > 0:
                lost = i+1
        
        return [dupe, lost]
        
        # B) Math Sum_expected=(n*[n+1])/2
        """
        n = len(nums)
        expectedSum = (n*(n+1)) // 2 # expected sum (formula)
        actualSum = sum(nums) # actual sum
        setSum = sum(set(nums)) # set of nums (without duplicate)

        duplicate = actualSum - setSum
        lost = expectedSum - setSum

        return [duplicate, lost]
        """